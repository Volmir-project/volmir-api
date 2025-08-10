from django.urls import path

from api.task.all_user_tasks.get_all_user_tasks_view import get_all_user_tasks_view

urlpatterns = [
    path('get-all-tasks/', get_all_user_tasks_view, name='get-all-tasks'),
]