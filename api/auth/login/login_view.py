from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import hashlib

from api.auth.login.login_logic import login_user
from api.pydantic_models.login.login_model import LoginModelRequest

@csrf_exempt
@require_http_methods(['POST'])
def login(login_request):
    login_request_data = json.loads(login_request.body)
    login_model_request = LoginModelRequest(
        email=login_request_data['email'],
        password=login_request_data['password'],
    )
    return login_user(login_model_request)