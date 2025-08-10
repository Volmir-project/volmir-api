from django.urls import path

from api.task.not_completed_task.not_completed_logic import not_completed_task

urlpatterns = [
    path('not-completed-task/', not_completed_task, name='not-completed-task'),
]