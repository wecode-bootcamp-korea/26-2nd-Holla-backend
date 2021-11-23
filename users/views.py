import requests, jwt

from django.http.response import JsonResponse
from django.views         import View

from users.models         import User
from django.conf          import settings

class KakaoSignInView(View):
    def get(self, request):
        try:
            access_token   = request.headers["Authorization"]
            
            kakao_response = requests.get("https://kapi.kakao.com/v2/user/me", \
                headers={"Authorization": f"Bearer {access_token}"})
            
            kakao_data = kakao_response.json()
            kakao_id   = kakao_data["id"]
            email      = kakao_data["kakao_account"]["email"]
            nickname   = kakao_data["properties"]["nickname"]

            obj, created = User.objects.get_or_create(
                kakao_id = kakao_id,
                email    = email,
                name     = nickname
            )
            
            status_code = 201 if created else 200

            results = {
                "name"  : obj.name,
                "email" : obj.email
            }

            jwt_payload  = {"id" : obj.id}
            access_token = jwt.encode(jwt_payload, settings.SECRET_KEY, algorithm = settings.ALGORITHM)
            
            return JsonResponse({
                    "message" : "SUCCESS", 
                    "results" : results, 
                    "access_token": access_token
                }, status=status_code)

        except KeyError:
            return JsonResponse({"message" : "TOKEN_OR_KEY_ERROR"}, status = 400)