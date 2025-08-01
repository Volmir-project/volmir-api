from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse

from api.models import User
from api.pydantic_models.login.login_model import LoginModelRequest


def login_user(login_request: LoginModelRequest) ->  JsonResponse:
    try:
        user = User.objects.filter(email=login_request.email).first()

        if not user:
            return JsonResponse({
                'message': 'User does not exist'
            }, status=404)
        if not check_password(login_request.password, user.password):
            return JsonResponse({
                'message': 'Password does not match'
            }, status=403)

        return JsonResponse({
            'success': True,
            'message': 'User logged in successfully',
            'user_id': str(user.user_id),
        })
    except Exception as e:
        return JsonResponse({
            'message': e
        }, status=500)