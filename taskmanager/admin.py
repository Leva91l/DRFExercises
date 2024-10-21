from django.contrib import admin

from taskmanager.models import Task, SubTask

admin.site.register(Task)
admin.site.register(SubTask)