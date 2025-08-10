from django.urls import path

from api.task.add_task.add_task_view import add_task_view

urlpatterns = [
    path('add-task/', add_task_view, name='add-task'),
]