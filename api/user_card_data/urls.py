from django.urls import path

from api.task.add_task.add_task_view import add_task_view

urlpatterns = [
    path('data/', add_task_view, name='user_card_data'),
]