from django.urls import path
from users.views import KakaoSignInView

app_name = 'users'
urlpatterns = [
    path('/kakao/signin', KakaoSignInView.as_view()),
] 