from django.contrib.auth.hashers import make_password
from django.db import transaction, IntegrityError
from django.http import JsonResponse

from api.models import User
from api.pydantic_models.signup.signup_model import SignupModelRequest


def signup_logic(request: SignupModelRequest) -> JsonResponse:
    try:

        if len(request.username) < 6:
            return JsonResponse({
                'error': 'Username needs to contain at least 6 characters.'
            }, status=400)

        if len(request.password1) < 8:
            return JsonResponse({
                'error': 'Password needs to be at least 8 characters.'
            }, status=400)

        if request.password1 != request.password2:
            return JsonResponse({
                'error': 'Passwords do not match'
            }, status=400)

        with transaction.atomic():
            new_user = User(
                username=request.username,
                email=request.email,
                password=make_password(request.password1),
            )
            new_user.save()

        return JsonResponse({
            'success': True,
            'message': 'User created successfully',
            'user_id': str(new_user.user_id),
        }, status=200)

    except IntegrityError:
        return JsonResponse({
            'error': 'User with this email or username already exists'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)
