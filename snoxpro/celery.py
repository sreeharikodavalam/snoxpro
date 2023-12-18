from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snoxpro.settings')

app = Celery('snoxpro', include=['events.tasks'])
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# app.autodiscover_tasks(['snoxpro', 'events'])

app.conf.beat_schedule = {
    'my-periodic-task': {
        'task': 'events.tasks.my_periodic_task',
        'schedule': crontab(minute='*'),  # Adjust as needed
    },
}

# Load the schedule from the settings
app.conf.timezone = 'UTC'
