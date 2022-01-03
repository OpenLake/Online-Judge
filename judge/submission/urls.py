from django.urls import path, include
from .views import *

urlpatterns = [
    path("submission/create/", SubmissionCreateAPI.as_view()),
]