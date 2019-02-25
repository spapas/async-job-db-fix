from django.db import models


class Task(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=128)
    url_length = models.PositiveIntegerField(blank=True, null=True)
    job_id = models.CharField(max_length=128, blank=True, null=True)
    result = models.CharField(max_length=128, blank=True, null=True)
