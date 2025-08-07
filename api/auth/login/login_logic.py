import datetime

from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
import jwt
from api.models import User
from api.pydantic_models.login.login_model import LoginModelRequest
from django.conf import settings


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

        token = jwt.encode({
            'user_id': str(user.user_id),
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2),
        }, settings.SECRET_KEY, algorithm='HS256')

        return JsonResponse({
            'success': True,
            'message': 'User logged in successfully',
            'token': token,
            'user_id': str(user.user_id),
        }, status=200)
    except Exception:
        return JsonResponse({
            'message': 'Error during login',
        }, status=500)