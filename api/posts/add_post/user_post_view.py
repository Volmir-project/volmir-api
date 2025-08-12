import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from api.posts.add_post.user_post_logic import user_post_logic
from api.pydantic_models.post_models.add_post_model.add_post_model import AddPostModel


@csrf_exempt
@require_http_methods(['POST'])
def user_post_view(request, user_id) -> JsonResponse:
    try:
        post_data = json.loads(request.body)

        post_model = AddPostModel(
            user_id=user_id,
            task_id=post_data['taskId'],
            post_body=post_data['postBody'],
        )

        return user_post_logic(post_model)
    except Exception:
        return JsonResponse({'success': False}, status=404)

