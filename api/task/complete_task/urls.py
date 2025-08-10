from django.urls import path

from api.task.complete_task.complete_task_logic import complete_task

urlpatterns = [
    path('complete-task/', complete_task, name='complete-task'),
]