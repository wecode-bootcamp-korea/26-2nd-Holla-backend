import unittest, jwt

from django.http    import response
from django.test    import TestCase, Client
from unittest.mock  import patch, MagicMock

from users.models   import User
from django.conf    import settings

class KakaoSignInTest(TestCase):
    def setUp(self):
        User.objects.create(
            id = 1,
            nickname = "카카오",
            name = "병철쓰",
            email = "wecode_kakao@naver.com",
            kakao_id = 234234
        )
        
    def tearDown(self):
        User.objects.all().delete()

    @patch('users.views.requests')
    def test_get_kakao_signin_user_exist_success(self, mocked_requests):
        client = Client()
        class MockedResponse:
            def json(self):
                return {
                    'id'          : 234234, 
                    'connected_at': '2020-12-03T05:31:36Z', 
                    'properties'  : {
                        'nickname'         : '병철쓰', 
                        'profile_image'    : 'http://k.kakaocdn.net/dn/bOugw5/btqJWTqzK7X/HG32V3SaqKbtNGIVl0dgKK/img_640x640.jpg', 
                        'thumbnail_image'  : 'http://k.kakaocdn.net/dn/bOugw5/btqJWTqzK7X/HG32V3SaqKbtNGIVl0dgKK/img_110x110.jpg'}, 
                        'kakao_account': {
                            'profile_needs_agreement': False, 
                            'profile': {
                                'nickname': '병철쓰', 
                                'thumbnail_image_url': 'http://123123.jpg', 
                                'profile_image_url': 'http://234234243.jpg', 
                        'is_default_image' : False
                        }, 
                        'has_email'            : True, 
                        'email_needs_agreement': False, 
                        'is_email_valid'       : True, 
                        'is_email_verified'    : True, 
                        'email'                : 'wecode_kakao@naver.com'
                        }}
 
        results = {
            "name"  : "병철쓰",
            "email" : "wecode_kakao@naver.com"
        }

        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {"HTTP_Authorization" : "guraDFDDGH454398"}
        access_token        = jwt.encode({"id" : 1}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        response            = client.get("/users/kakao/signin", **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message" : "SUCCESS", "results" : results, "access_token" : access_token})

    @patch('users.views.requests')
    def test_get_kakao_signin_user_not_exist_success(self, mocked_requests):
        client = Client()
        class MockedResponse:
            def json(self):
                return {
                    'id'          : 1547717464, 
                    'connected_at': '2020-12-03T05:31:36Z', 
                    'properties'  : {
                        'nickname'         : '김코드', 
                        'profile_image'    : 'http://k.kakaocdn.net/dn/bOugw5/btqJWTqzK7X/HG32V3SaqKbtNGIVl0dgKK/img_640x640.jpg', 
                        'thumbnail_image'  : 'http://k.kakaocdn.net/dn/bOugw5/btqJWTqzK7X/HG32V3SaqKbtNGIVl0dgKK/img_110x110.jpg'}, 
                        'kakao_account': {
                            'profile_needs_agreement': False, 
                            'profile': {
                                'nickname': '김코드', 
                                'thumbnail_image_url': 'http://123123.jpg', 
                                'profile_image_url': 'http://234234243.jpg', 
                        'is_default_image' : False
                        }, 
                        'has_email'            : True, 
                        'email_needs_agreement': False, 
                        'is_email_valid'       : True, 
                        'is_email_verified'    : True, 
                        'email'                : 'wecode10101010@gmail.com'
                        }}
      
        results = {
            "name"  : "김코드",
            "email" : "wecode10101010@gmail.com"
        }
        
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {"HTTP_Authorization" : "guraDFDDGH454398"}
        access_token        = jwt.encode({"id" : 2}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        response            = client.get("/users/kakao/signin", **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message" : "SUCCESS", "results" : results, "access_token" : access_token})        

    @patch('users.views.requests')
    def test_kakao_signin_exist_not_token_failed(self, mocked_requests):
        client = Client()
        headers  = {}
        response = client.get("/users/kakao/signin", **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message" : "TOKEN_OR_KEY_ERROR"})        