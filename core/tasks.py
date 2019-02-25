import requests
from .models import Task
from rq import get_current_job
from django_rq import job


@job
def get_url_length(task_id):
    job = get_current_job()
    task = Task.objects.get(
        id=task_id
    )
    response = requests.get(task.url)
    task.url_length = len(response.text)
    task.job_id = job.get_id()
    task.result = 'OK'
    task.save()
