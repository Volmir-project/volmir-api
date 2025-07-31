from django.urls import path

from api.auth.signup import signup_view

urlpatterns = [
    path('', signup_view.signup, name='signup'),
]