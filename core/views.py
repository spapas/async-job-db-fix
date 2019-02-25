from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import TaskForm
from .tasks import get_url_length
from .models import Task
from rq.job import Job
import django_rq
import datetime

import time
from django.db import transaction


class TasksHomeFormView(FormView):
    form_class = TaskForm
    template_name = 'tasks_home.html'
    success_url = '/'

    def form_valid(self, form):
        task = Task.objects.create(url=form.cleaned_data['url'])

        # get_url_length.delay(task.id)
        transaction.on_commit(lambda: get_url_length.delay(task.id))

        time.sleep(1)

        return super(TasksHomeFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(TasksHomeFormView, self).get_context_data(**kwargs)
        ctx['tasks'] = Task.objects.all().order_by('-created_on')
        return ctx
