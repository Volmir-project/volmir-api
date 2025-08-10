from django.urls import path

from api.task.delete_task.delete_task_logic import delete_task

urlpatterns = [
    path('delete-task/', delete_task, name='delete-task'),
]