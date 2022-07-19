from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_feeder.settings')

app = Celery('news_feeder')

app.conf.enable_utc = False
app.conf.update(timezone='Asia/Dhaka')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'fetch_news_from_newsapi': {
        'task': 'update_news',
        # 'schedule': crontab(minute='*/10'),
        'schedule': 10,
        'options': {
            'expires': 8*60,
        },
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
