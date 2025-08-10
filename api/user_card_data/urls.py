from django.urls import path

from api.user_card_data.get_user_card_data import get_user_card_data

urlpatterns = [
    path('data/', get_user_card_data, name='user_card_data'),
]