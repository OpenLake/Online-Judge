from django.db.models.signals import post_save
from django.dispath mport receiver
from .models import Submission

@receiver(post_save, sender=Submission)
def run_code_in_background