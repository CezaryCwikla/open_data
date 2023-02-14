# import os
# from celery import Celery
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'open_data.settings')
#
# app = Celery('open_data')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()