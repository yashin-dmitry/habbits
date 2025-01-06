from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-reminders-every-day': {
        'task': 'habits.tasks.send_reminder',
        'schedule': crontab(minute=0, hour=0),  # Каждый день в полночь
    },
}