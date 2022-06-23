"""
Файл настроек Celery
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'script_db.settings')

app = Celery('script_db',)

app.conf.imports = ('data_collect.tasks',)

app.conf.beat_schedule = {
    'update database': {
        'task': 'data_collect.tasks.collect_data',
        'schedule': crontab(minute='*/1')
    },
}

app.autodiscover_tasks()
