from celery import shared_task
from .models import Submission
from question.models import Question, Test
import sys

@shared_task
def queue_submission(submission_id):
    submission = Submission.object.get(id=submission_id)
    submission.status = "processing"
    submission.save()
    code_file_path = submission.code_file.path
    code_file_name = submission.code_file.name
    filename = code_file_name.split("/")[1].split(".")[0]
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("code." + str(filename), str(code_file_path))
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        # pass parameters for submit, from test file of question
        for test_obj in Test.objects.filter(question=submission.question):
            input_test_file = test_obj.input_file
            foo.submit()
    # get the codefile
    # run the code file with list of test case
    #   if invalid file format, SumissionTest status is NA.
    #   if run for more than 2 mnin, TLE
    #   if run but incorrrect answer, status is WA (create output_file)
    #