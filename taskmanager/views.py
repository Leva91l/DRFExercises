from rest_framework import viewsets, generics, permissions


from taskmanager.models import Task, SubTask
from taskmanager.serializers import TaskSerializer, SubTaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer




class SubTaskAPIList(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SubTaskAPIUpdate(generics.UpdateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer


class SubTaskAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = (permissions.IsAdminUser,)