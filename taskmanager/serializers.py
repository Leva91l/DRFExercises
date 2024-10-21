from rest_framework import serializers

from taskmanager.models import Task, SubTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'execution_status')


class SubTaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = SubTask
        fields = ('title', 'description', 'execution_status', 'time_created', 'task', 'user')
