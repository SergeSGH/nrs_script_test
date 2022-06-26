from django.shortcuts import redirect, render

from .models import Record
from .tasks import check_deadlines, collect_data


def OnePageView(request):
    template = 'index.html'
    records_count = Record.objects.all().count()
    context = {
        'records_count': records_count
    }
    return render(request, template, context)


def UpdateDB(request):
    collect_data()
    return redirect('/')


def UpdateDL(request):
    check_deadlines()
    return redirect('/')
