import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from api.auth.signup.signup_logic import signup_logic
from api.pydantic_models.signup.signup_model import SignupModelRequest


@csrf_exempt
@require_http_methods(['POST'])
def signup(signup_request_data) -> JsonResponse:
    signup_request_data = json.loads(signup_request_data.body)
    signup_model_request = SignupModelRequest(
        email=signup_request_data['email'],
        first_name=signup_request_data['firstName'],
        last_name=signup_request_data['lastName'],
        username=signup_request_data['username'],
        password1=signup_request_data['password1'],
        password2=signup_request_data['password2'],
    )
    return signup_logic(signup_model_request)