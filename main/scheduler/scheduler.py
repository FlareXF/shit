from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
from main.models import Sites
from django.utils import timezone
import sys

import pythonping

def check_site(url):
    ping = pythonping.ping(target = url, count = 5, timeout = 2)
    return ping.rtt_avg_ms


def update_site_values():
    values_number = 24

    sites = Sites.objects.all()
    for site in sites:
        vals = site.values()
        if len(vals['time']) < 24:
            for i in range(24-len(vals['time'])):
                vals[str(timezone.now)] = check_site(site.url)

    pass

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(update_site_values, 'interval', hours=24, name='clean_accounts', jobstore='default')
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)