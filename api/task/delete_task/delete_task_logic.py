from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from api.models import Task


@csrf_exempt
@require_http_methods(['POST'])
def delete_task(request, task_id):
    try:
        with transaction.atomic():
            task = Task.objects.get(task_id=task_id)
            print(task)
            task.delete()

            return JsonResponse({
                'success': True,
            })
    except Task.DoesNotExist:
        return JsonResponse({'success': False}, status=404)
    except Exception:
        return JsonResponse({'success': False}, status=500)