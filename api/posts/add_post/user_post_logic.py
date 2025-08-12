import datetime

from django.db import transaction
from django.http import JsonResponse

from api.models import Post, User, Task
from api.pydantic_models.post_models.add_post_model.add_post_model import AddPostModel


def user_post_logic(post_model: AddPostModel) -> JsonResponse:
    try:
        with transaction.atomic():
            user = User.objects.filter(user_id=post_model.user_id).first()
            task = Task.objects.filter(task_id=post_model.task_id).first()

            new_post = Post(
                post_body=post_model.post_body,
                user_id=user.user_id,
                task_id=task.task_id,
            )

            new_post.save()

            return JsonResponse({'success': True}, status=201)
    except:
        return JsonResponse({'success': False}, status=404)
