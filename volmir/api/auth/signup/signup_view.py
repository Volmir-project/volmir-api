import hashlib
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from pydantic import ValidationError

from api.models.signup.signup_model import SignupModelRequest


@csrf_exempt
@require_http_methods(['POST'])
def signup(signup_request_data):
    signup_request_data = json.loads(signup_request_data.body)
    hashed_password_1 = hashlib.sha256()
    hashed_password_2 = hashlib.sha256()
    hashed_password_1.update(signup_request_data['password1'].encode())
    hashed_password_2.update(signup_request_data['password2'].encode())
    signup_model_request = SignupModelRequest(
        email=signup_request_data['email'],
        username=signup_request_data['username'],
        password1=hashed_password_1.hexdigest(),
        password2=hashed_password_2.hexdigest()
    )
    if signup_model_request.password1 != signup_model_request.password2:
        return JsonResponse({'error': 'Passwords do not match'}, status=400)
    try:
        SignupModelRequest.model_validate(signup_model_request)
    except ValidationError as e:
        return JsonResponse({'error': e.message}, status=400)
    print(signup_model_request.model_dump_json(indent=2))
    return JsonResponse({})