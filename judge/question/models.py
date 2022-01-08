from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    class Meta:
       verbose_name = "Question"
       verbose_name_plural = "Questions"

class Test(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="question"
    )
    test = models.TextField()
    correct_answer = models.TextField()
    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Tests"
 