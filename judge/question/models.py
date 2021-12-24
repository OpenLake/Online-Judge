from django.db import models

class Question(models.Model):
    statement = models.TextField()
    
    class Meta:
       verbose_name = "Question"
       verbose_name_plural = "Questions"
 