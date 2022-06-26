import os
from django.shortcuts import redirect, render

from .models import Record
from .tasks import check_deadlines, collect_data
from .forms import TelegramIDForm


def OnePageView(request):
    template = 'index.html'
    records_count = Record.objects.all().count()
    form = TelegramIDForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        telegram_id = form.cleaned_data['telegram_id']
        if telegram_id != 0:
            with open('telegram_id.txt', 'w', encoding="utf-8") as f:
                f.write(str(telegram_id))
        else:
            os.remove('telegram_id.txt')
        form = TelegramIDForm()
    else:
        if os.path.isfile('telegram_id.txt'):
            with open('telegram_id.txt', 'r', encoding="utf-8") as f:
                telegram_id = f.read()
        else:
            telegram_id = 'не установлен'
    context = {
        'records_count': records_count,
        'telegram_id': telegram_id,
        'form': form
    }
    return render(request, template, context)


def UpdateDB(request):
    collect_data()
    return redirect('/')


def UpdateDL(request):
    check_deadlines()
    return redirect('/')
