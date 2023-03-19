from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):

    task_name = models.CharField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now())
    owner = models.ForeignKey(User, related_name='tasks')
