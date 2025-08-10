from django.db import transaction
from django.http import JsonResponse

from api.models import Task, User
from api.pydantic_models.task_models.add_task.add_task_model import AddTaskModelRequest


def add_task(add_task_model: AddTaskModelRequest) -> JsonResponse:
    with transaction.atomic():
        user = User.objects.filter(user_id=add_task_model.user_id).first()
        new_task = Task(
            task_title=add_task_model.task_title,
            task_description=add_task_model.task_description,
            task_deadline=add_task_model.task_deadline,
            task_xp=add_task_model.task_xp,
            user=user,
        )
        new_task.save()

    return JsonResponse({'task_id': new_task.task_id}, status=201)
