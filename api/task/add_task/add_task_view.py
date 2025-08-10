import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from api.pydantic_models.task_models.add_task.add_task_model import AddTaskModelRequest
from api.task.add_task.add_task_logic import add_task


@csrf_exempt
@require_http_methods(['POST'])
def add_task_view(request, user_id) -> JsonResponse:
    add_task_request = json.loads(request.body)

    add_task_model = AddTaskModelRequest(
        user_id=user_id,
        task_title=add_task_request["taskTitle"],
        task_description=add_task_request["taskDescription"],
        task_deadline=add_task_request["taskDeadline"],
        task_xp=add_task_request["taskXp"],
    )

    add_task_response = add_task(add_task_model)

    if not add_task_response:
        return JsonResponse({'task_id': add_task_model.task_id}, status=404)
    return add_task_response

