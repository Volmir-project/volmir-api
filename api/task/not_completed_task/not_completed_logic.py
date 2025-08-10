from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from api.models import Task, User


@csrf_exempt
@require_http_methods(['POST'])
def not_completed_task(request, task_id) -> JsonResponse:
    try:
        with transaction.atomic():
            task = Task.objects.get(task_id=task_id)
            task.is_active = True
            task.save()

            user = User.objects.get(user_id=task.user_id)
            user.xp -= task.task_xp
            user.save()

            return JsonResponse({'success': True}, status=200)
    except Task.DoesNotExist:
        return JsonResponse({'success': False}, status=404)
    except Exception:
        return JsonResponse({'success': False}, status=500)