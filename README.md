# online-judge

1. Make a virtal env
2. Pip install -r requirements.txt
3. Configure database of your choice
4. Load sample questions : "python manage.py loaddata data_question.json"
5. Load sample test_case : "python managepy loaddata data_test.json"

# start your worker
1. Setup Rabbitmq broker
2. start your worker: celery -A judge worker -l debug