from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
from main.models import Sites
from django.utils import timezone, dateformat
import sys
import re

import pythonping

def check_site(url):
    ping = pythonping.ping(target = url, count = 1, timeout = 1, verbose=False)
    return ping.rtt_avg_ms


def update_site_values():
    values_number = 24
    sites = Sites.objects.all()
    for site in sites:
        vals = site.values
        if len(vals) < values_number:
            url_with_protocol = site.url
            url = re.sub(r"https?://", '', url_with_protocol)
            formatted_date = dateformat.format(timezone.now(), 'G:i')
            vals[str(formatted_date)] = check_site(url)
            site.save()
        else:
            vals.pop(list(vals.keys())[0])
            url_with_protocol = site.url
            url = re.sub(r"https?://", '', url_with_protocol)
            formatted_date = dateformat.format(timezone.now(), 'G:i')
            vals[str(formatted_date)] = check_site(url)
            site.save()

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(update_site_values, 'interval', minutes=1, name='clean_accounts', jobstore='default')
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)