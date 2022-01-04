import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "judge.settings")

app = Celery("judge")
app.config_from_object("django.conf:settings", namespace="CELERY")
# app.conf.update(
#     task_serializer='pickle',
#     result_serializer='pickle'
# )
app.autodiscover_tasks()