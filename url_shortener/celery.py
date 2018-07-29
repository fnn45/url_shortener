import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'url_shortener.settings')

app = Celery('scheduler')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'celery_test_heartbeat': {
        'task': 'scheduler.tasks.heartbeat',
        'schedule': crontab(minute="*"),
    },
    'delete_old_urls': {
            'task': 'scheduler.tasks.delete_old_urls',
            'schedule': crontab('*/5'), # every 5 minutes
        }
}
