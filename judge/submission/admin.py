from django.contrib import admin
from .models import Submission, SubmissionTest

# Register your models here.
admin.site.register(Submission)
admin.site.register(SubmissionTest)