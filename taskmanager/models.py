from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    execution_status = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title


class SubTask(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    execution_status = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title