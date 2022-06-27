"""
Файл настроек Celery
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'script_db.settings')

app = Celery('script_db', broker='amqp://rabbitmq:rabbitmq@rabbit:5672')

app.conf.imports = ('data_collect.tasks',)

app.conf.beat_schedule = {
    'update database': {
        'task': 'data_collect.tasks.collect_data',
        'schedule': crontab(minute='*/1')
    },
    'update deadlines': {
        'task': 'data_collect.tasks.check_deadlines',
        'schedule': crontab(hour=8, minute=0, day_of_week=1)
    },
}

app.autodiscover_tasks()
