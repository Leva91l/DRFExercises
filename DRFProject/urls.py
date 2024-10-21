from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from taskmanager.views import TaskViewSet, SubTaskAPIList, SubTaskAPIUpdate, SubTaskAPIDestroy

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/subtasks/', SubTaskAPIList.as_view()),
    path('api/v1/subtasks/<int:pk>/', SubTaskAPIUpdate.as_view()),
    path('api/v1/subtasksdelete/<int:pk>/', SubTaskAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
