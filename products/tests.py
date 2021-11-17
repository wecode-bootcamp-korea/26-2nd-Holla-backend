from django.http import response
from django.test import TestCase, Client

from .models import Author, Product

class ProductTest(TestCase):
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