import jwt

from django.test    import TestCase, Client
from django.conf    import settings

from .models        import Author, Product
from orders.models  import ShoppingHistory
from users.models   import User
from reviews.models import Review

class ProductTest(TestCase):
    maxDiff = None
    def setUp(self):
        self.client = Client()
        Product.objects.create(
            id          = 1,
            intro       = "최고의 베스트셀러",
            title       = "100가지 장소의 보금자리",
            price       = "5800.00",
            description = "지금도 계속되고 있는 세계 각지로의 여행",
            image_url   = "https://drive.google.com/file/d/1Q3vcfEg-1Svrh78YF7QmP9oPMW-EErfA/view?usp=sharing"
        )

        Author.objects.create(
            id           = 1,
            name         = "이태훈",
            image_url    = "https://images.unsplash.com/photo-1568602471122-7832951cc4c5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80",
            introduction = "최고의 베스트셀러 작가이다",
            product_id   = 1
        )
    
    def tearDown(self):
        Product.objects.all().delete()
        Author.objects.all().delete()

    def test_product_get_success(self):
        response = self.client.get('/products/1')
        
        self.assertEqual(response.json(),
            {
                "product": [
                    {
                    "image_url"    : "https://drive.google.com/file/d/1Q3vcfEg-1Svrh78YF7QmP9oPMW-EErfA/view?usp=sharing",
                    "intro"        : "최고의 베스트셀러",
                    "title"        : "100가지 장소의 보금자리",
                    "price"        : "5800.00",
                    "description"  : "지금도 계속되고 있는 세계 각지로의 여행",
                    "author": {
                        "profile_url": "https://images.unsplash.com/photo-1568602471122-7832951cc4c5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80",
                        "name": "이태훈",
                        "introduction": "최고의 베스트셀러 작가이다"
                        }
                    }
                ]
            }
        )
        self.assertEqual(response.status_code, 200)

    def test_get_product_does_not_exitst_error(self):
        response = self.client.get('/products/7')

        self.assertEqual(response.json(), {"message" : "PRODUCT_DOES_NOT_EXIST"})
        self.assertEqual(response.status_code, 404)

class MainTotalTest(TestCase):
    maxDiff = None
    
    def setUp(self):
        User.objects.create(
            id       = 1,
            email    = "wecode@gmail.com",
            nickname = "테스트",
            name     = "김테스",
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

        Author.objects.create(
            id           = 1,
            image_url    = "h",
            name         = "작가",
            introduction = "인트로덕션",
            product_id   = 1
        )

        Review.objects.create(
            id         = 1,
            user_id    = 1,
            product_id = 1,
            text       = "텍스트",
            rating     = 5
        )

        ShoppingHistory.objects.create(
            id         = 1,
            user_id    = 1,
            product_id = 1
        )

        self.token = jwt.encode({
            'id' : User.objects.get(id=1).id
            }, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    def tearDown(self):
        User.objects.all().delete()
        Product.objects.all().delete()
        Author.objects.all().delete()
        Review.objects.all().delete()
        ShoppingHistory.objects.all().delete()

    def test_get_main_total_success(self):
        client = Client()
        header = {"HTTP_Authorization" : self.token}
        response = client.get("/", **header)
        results = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(results, {
            'message': 'SUCCESS', 
            'results': {
                'name': '김테스', 
                'recommend_books': [
                    {
                        'id': 1, 
                        'product_images': 'h', 
                        'intro': '인트로'
                    }
                ], 
                'realtime_reviews': [
                    {
                        'id': 1, 
                        'product_images': 'h', 
                        'text': '텍스트', 
                        'name': '김테스'
                    }
                ], 
                'book_of_the_month': [
                    {
                        'id': 1, 
                        'product_images': 'h', 
                        'title': '타이틀', 
                        'author': '작가', 
                        'author_images': 'h'
                    }
                ]
            }
        })