from celery import shared_task
from .models import Submission, SubmissionTest
from question.models import Question, Test
import sys
import json

@shared_task
def queue_submission(submission_id):
    submission = Submission.objects.get(id=submission_id)
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
        temp_submission_status = "AC"
        for test_obj in Test.objects.filter(question=submission.question.id):
            input_test = json.loads(test_obj.test)
            print(input_test)
            print(type(input_test))
            # run the code 
            output = foo.submit(*input_test)
            # create a submit tet object
            submit_test = SubmissionTest.objects.create(test=test_obj, submission=submission, output=json.dumps(output))
            if submit_test.output == test_obj.correct_answer:
                submit_test.status = "AC"
                submit_test.save()
            elif submit_test.output != "" and submit_test.output != test_obj.correct_answer:
                submit_test.status = "WA"
                submit_test.save()
                temp_submittion_status = "WA"
        submission.status = temp_submission_status
        submission.save()
        return "No run time error"
    except Exception as e:
        error = str(e)
        print("run time error")
        return error
