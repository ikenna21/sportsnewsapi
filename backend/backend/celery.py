
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')



app = Celery('backend')

app.conf.beat_schedule = {
    'fetch-feeds-every-15':{
        'task': 'api.tasks.index',
        'schedule': crontab(minute='*/15')
    }
}

app.conf.timezone = 'UTC'

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

if __name__ == "__main__":
    app.start()