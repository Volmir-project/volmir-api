from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import hashlib
from api.pydantic_models.login.login_model import LoginModelRequest

@csrf_exempt
@require_http_methods(['POST'])
def login(login_request_data):
    login_request_data = json.loads(login_request_data.body)
    hash_obj = hashlib.sha256()
    hash_obj.update(login_request_data['password'].encode())
    login_model_request = LoginModelRequest(
        email=login_request_data['email'],
        password=hash_obj.hexdigest(),
    )
    print(login_model_request.model_dump_json(indent=2))
    return JsonResponse({})