from django.urls import path

from api.posts.get_all_posts.get_all_posts_view import get_all_posts_view

urlpatterns = [
    path('get-all-posts/', get_all_posts_view, name='get-all-posts'),
]