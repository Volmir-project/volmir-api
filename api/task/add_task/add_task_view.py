import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from api.pydantic_models.task_models.add_task.add_task_model import AddTaskModel


@csrf_exempt
@require_http_methods(['POST'])
def add_task(request) -> JsonResponse:
    add_task_request = json.loads(request.data)

    add_task_model = AddTaskModel(
        task_title=add_task_request["task_title"],
        task_description=add_task_request["task_description"],
        task_deadline=add_task_request["task_deadline"],
        task_xp=add_task_request["task_xp"],
    )

