from django.urls import path
from api.auth.login import login_view

urlpatterns = [
    path('', login_view.login, name='login'),
]