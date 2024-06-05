import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyShop.settings')

app = Celery('MyShop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
