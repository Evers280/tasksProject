from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TasksViewSet

routers = DefaultRouter()
routers.register('tasks', TasksViewSet, basename='tasks')

urlpatterns = [
    path('', include(routers.urls))
]