from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=250)
    test_count = models.PositiveIntegerField()
    content = models.TextField()
    test = models.TextField()
    class Meta:
       verbose_name = "Question"
       verbose_name_plural = "Questions"
 