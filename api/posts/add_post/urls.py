from django.urls import path

from api.posts.add_post.user_post_view import user_post_view

urlpatterns = [
    path('add-post/', user_post_view, name='user-post'),
]