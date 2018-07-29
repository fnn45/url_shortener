import os
import platform

from datetime import date, timedelta, datetime

from url_shortener.celery import app
from shortener.models import UrlDetails

@app.task
def heartbeat():
    with open('./share/celery_logs/heartbeat.txt', 'a') as f:
        f.write('<< {} >>  {} \n'.format(platform.platform(), datetime.now()))

@app.task
def delete_old_urls():
    boundary_date = date.today() - timedelta(14)
    delete_qs = UrlDetails.objects.filter(timestamp__lt=boundary_date)
    delete_qs.delete()








