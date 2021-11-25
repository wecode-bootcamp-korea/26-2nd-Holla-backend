import jwt

from django.test             import TestCase, Client
from django.conf             import settings

from reviews.models  import Review
from users.models    import User
from products.models import Product

class ReviewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        User.objects.create(
            id       = 1,
            email    = "wecode@gmail.com",
            name     = "김코드",
            nickname = "김코드",
            kakao_id = 234234
        )

        Product.objects.create(
            id          = 1,
            intro       = "인트로",
            title       = "타이틀",
            price       = 50000,
            description = "설명",
            image_url   = "h",
            genre       = "멜로"
            )

        Review.objects.create(
            id         = 1,
            rating     = 3.0,
            user_id    = 1,
            text       = "리뷰 유닛 테스트 중입니다.",
            product_id = 1,
        )

        self.token = jwt.encode({
            'id' : User.objects.get(id=1).id,
        }, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        
    def tearDown(self):
        Review.objects.all().delete()
        User.objects.all().delete()
        Product.objects.all().delete()

    def test_get_review_success(self):
        client = Client()
        
        response = client.get("/reviews/1")
        
        self.assertEqual(response.json(),
        {
            "result" : {
                "total_reviews" : 1,
                "avg_rating" : 3.0,
                "reviews" : [
                    {
                        "id"   : 1,
                        "name" : "김코드",
                        "date" : "2021.11.25 12:11",
                        "text" : "리뷰 유닛 테스트 중입니다."
                    }
                ]
            }
        })

        self.assertEqual(response.status_code, 200)

    def test_post_review_success(self):
        client    = Client()
        headers   = {"HTTP_Authorization" : self.token}
        post_data = {"rating" : 3.0, "text" : "텍스트"}
        
        response  = client.post("/reviews/1",  
        post_data, content_type='application/json', **headers)
        
        self.assertEqual(response.json(), {"message" : "SUCCESS"})
        self.assertEqual(response.status_code, 201)

    def test_delete_review_success(self):
        client   = Client()
        
        headers  = {"HTTP_Authorization" : self.token}
        
        response = client.delete("/reviews/1", **headers)
        
        self.assertEqual(response.json(), {"message" : "SUCCESS"})
        self.assertEqual(response.status_code, 200)             