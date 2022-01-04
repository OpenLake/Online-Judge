from django.db import models
from question.models import Question, Test
from .utils import code_file_name
# submission : id, code_file_path, created_at, status, question_id

# submission_test : test_id, submission_id, output_file
class Submission(models.Model):
    code_file = models.FileField(
        upload_to=code_file_name,
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status_choices = (
        ("TLE", "TLE"), 
        ("WA", "WA"), 
        ("AC", "AC"), 
        ("procesing", "processing"), 
        ("queue", "queue"),
        ("NA", "NA")
        )
    status = models.CharField(
        choices=status_choices, 
        max_length=20,
        default="queue"
        )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="submission",
    )
    class Meta:
       verbose_name = "Submission"
       verbose_name_plural = "Submissions"
    

class SubmissionTest(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name="submission_test",
    )
    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name="submission_test",
    )
    output_file = models.FilePathField(
        path="submission_test", 
        unique=True,
    )
    # NA - Not executed, runtime error
    status_choices = (
        ("TLE", "TLE"), 
        ("WA", "WA"), 
        ("AC", "AC"),
        ("NA", "NA"),
        )
    status = models.CharField(
        choices=status_choices, 
        max_length=20,
        default="NA"
        )
    class Meta:
       verbose_name = "Submission Test"
       verbose_name_plural = "Submission Tests"