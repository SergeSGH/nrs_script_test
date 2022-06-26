import datetime as dt
import itertools
import os

import apiclient.discovery
import httplib2
import requests
import xmltodict
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Bot

from .models import Record

load_dotenv()

date_format_test = '%d.%m.%Y'
date_format_cb = '%d/%m/%Y'
CREDENTIALS_FILE = 'nrsss-354115-e9688b1f5538.json'
spreadsheetId = '1nokg7tMCgLYMGpgky7nVNQlMZrO-1ZgHKr09m66wmr4'
block_size = 100


def str_is_number(s):
    """ Returns True if string is a number. """
    return s.replace('.', '', 1).isdigit()


def date_from_text(date_text):
    """ Returns date in datetime format from string """
    try:
        return dt.datetime.strptime(date_text, date_format_test)
    except ValueError:
        return False


from script_db.celery import app


@app.task
def check_deadlines():
    """ Collects records with deadline today from the db and sends message """
    token = os.getenv('TELEGRAM_TOKEN')
    if os.path.isfile('telegram_id.txt'):
        with open('telegram_id.txt', 'r', encoding="utf-8") as f:
            chat_id = f.read()
    else:
        chat_id = 0
    chat_id = os.getenv('CHAT_ID')
    bot = Bot(token=token)
    records_for_today = Record.objects.filter(delivery_date=dt.date.today())
    if records_for_today.count() != 0:
        message = 'Заказы на сегодня\n'
        for record in records_for_today:
            message += '№ заказа: {0}, стоимость: {1} руб.\n'.format(
                record.order_num, record.cost_rub
            )
    else:
        message = 'Заказов на сегодня нет\n'
    if chat_id:
        bot.send_message(chat_id, message)


@app.task
def collect_data():
    """ Reads data from Google spreadsheet and updates database """

    # clean the database before collection
    Record.objects.all().delete()

    # take USD rate from the CB site
    today_str = dt.datetime.today().strftime(date_format_cb)
    url = ('https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={0}'
           '&date_req2={0}&VAL_NM_RQ=R01235').format(today_str)
    try:
        response = requests.get(url)
        usd_data = xmltodict.parse(response.content)
    except Exception:
        usd_data = {}
    USD_RATE_STR = usd_data.get('ValCurs', {}).get('Record', {}).get('Value', {})
    if isinstance(USD_RATE_STR, str):
        USD_RATE_STR = USD_RATE_STR.replace(',', '.')
        if str_is_number(USD_RATE_STR):
            USD_RATE = float(USD_RATE_STR)
        else:
            USD_RATE = 0
    else:
        USD_RATE = 0

    # take USD rate from the CB site
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                           'https://www.googleapis.com/auth/drive']
    )
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

    # access the spreadsheet and see the number of rows in it
    results_ss = service.spreadsheets().get(
        spreadsheetId=spreadsheetId
    ).execute()
    row_count = results_ss['sheets'][0]['properties']['gridProperties']['rowCount']

    # start reading the spreadsheet by blocks
    counter = itertools.count(block_size, block_size)
    while True:
        block_end = next(counter)
        if block_end - block_size + 1 > row_count:
            break
        if block_end > row_count:
            block_end = row_count
        range = 'Лист1!A{0}:D{1}'.format(
            block_end - block_size + 1, block_end
        )
        results_block = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId, range=range
        ).execute()
        rows = results_block.get('values', [])
        if len(rows) == 0:
            break
        # after reading rows in the block write data to the db
        for row in rows:
            record_data = {}
            if row[0].isdecimal():  # check if format is correct for the 1st column
                record_data['num'] = int(row[0])
                if row[1].isdecimal():  # check if format is correct for the 2nd column
                    record_data['order_num'] = int(row[1])
                    if str_is_number(row[2]):  # check if format is correct for the 3rd column
                        record_data['cost'] = round(float(row[2]), 0)
                        date = date_from_text(row[3])  # see if date is in correct format
                        if date:
                            record_data['delivery_date'] = date
                            # if we cannot read the USD rate from the CB site the RUR cost is zero
                            if USD_RATE != 0:
                                record_data['cost_rub'] = round(float(record_data['cost']
                                                                * USD_RATE), 1)
                            else:
                                record_data['cost_rub'] = 0
                            new_record = Record.objects.create(**record_data)
                            new_record.save()
    return Record.objects.all()
