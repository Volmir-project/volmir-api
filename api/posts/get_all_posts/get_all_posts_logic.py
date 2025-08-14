from django.http import JsonResponse

from api.models import Post
from api.pydantic_models.post_models.get_all_posts_model.get_all_posts_model import GetAllPostsModel, Task, Comment


def get_all_posts_logic(user_id) -> JsonResponse:
    try:
        posts = Post.objects.filter(user_id=user_id).select_related('task', 'user').prefetch_related().all()

        posts_data: list = []
        for post in posts:

            if hasattr(post, 'task'):
                linked_task = Task(
                    task_id=post.task_id,
                    task_title=post.task.task_title,
                    task_description=post.task.task_description,
                    task_deadline=post.task.task_deadline,
                    task_xp=post.task.task_xp,
                    is_active=post.task.is_active,
                )

            post_model = GetAllPostsModel(
                linked_task=linked_task,
                full_name=f"{post.user.first_name} {post.user.last_name}",
                post_body=post.post_body,
                postLikesCount=0,
                postComments=[Comment(
                    comment_creator="",
                    comment_content="",
                )]
            )
            posts_data.append(post_model.dict())
        return JsonResponse({
            'success': True,
            'data': posts_data
        }, status=200, safe=False)
    except Exception:
        return JsonResponse({'success': False}, status=404)