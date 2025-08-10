import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from api.models import Task
from api.pydantic_models.task_models.get_all_user_tasks.get_all_user_tasks_model import UserTaskModel, AllUserTasksModel


@csrf_exempt
@require_http_methods(['POST'])
def get_all_user_tasks_view(request, user_id) -> JsonResponse:
    all_tasks = Task.objects.filter(user=user_id).all()

    all_user_tasks: list[UserTaskModel] = [UserTaskModel(
        task_id=task.task_id,
        task_title=task.task_title,
        task_description=task.task_description,
        task_deadline=task.task_deadline,
        task_xp=task.task_xp,
        is_active=task.is_active,
    ) for task in all_tasks]

    tasks = AllUserTasksModel(all_tasks=all_user_tasks)
    if tasks:
        return JsonResponse({
            'success': True,
            'all_tasks': json.loads(tasks.model_dump_json())
        }, safe=False, status=200)
    return JsonResponse([], safe=False, status=404)