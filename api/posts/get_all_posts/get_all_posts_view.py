import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from api.posts.get_all_posts.get_all_posts_logic import get_all_posts_logic


@csrf_exempt
@require_http_methods(['POST'])
def get_all_posts_view(request, user_id) -> JsonResponse:
    try:
        return get_all_posts_logic(user_id)
    except Exception:
        return JsonResponse({'success': False}, status=404)

