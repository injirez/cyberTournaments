import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cyberTournaments.settings')

app = Celery('cyberTournaments')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'addDotaWeplay': {
        'task': 'Dota.tasks.addDotaWeplay',
        'schedule': 40.0
    },
    'addDotaGamelix': {
        'task': 'Dota.tasks.addDotaGamelix',
        'schedule': 40.0
    },
    'addDotaCmode': {
        'task': 'Dota.tasks.addDotaCmode',
        'schedule': 40.0
    }
}