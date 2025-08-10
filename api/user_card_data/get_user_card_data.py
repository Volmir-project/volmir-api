from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from api.models import User
from api.pydantic_models.user_card_data_response.user_card_data_response import UserCardDataResponse

@csrf_exempt
@require_http_methods(['GET'])
def get_user_card_data(user_card_request, user_id) -> JsonResponse:
    user_data = User.objects.filter(user_id=user_id).first()
    if not user_data:
        return JsonResponse({"error": "User does not exist"}, status=404)

    user_card_data = UserCardDataResponse(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        username=user_data.username,
        xp=user_data.xp,
    )
    return JsonResponse(user_card_data.dict(), status=200)
