import jwt, requests
from django.test import TestCase, Client

from orders.models   import ShoppingCart, OrderStatus, PaymentType
from products.models import Product, Author
from users.models    import User
from django.conf     import settings

class CartGetTest(TestCase):
    maxDiff = None
    def setUp(self):
        self.client = Client()

        User.objects.create(
            id       = 1,
            email    = 'qudans@naver.com',    
            name     = '김코드',  
            nickname = '김코드',
            kakao_id = 123456
        )

        Product.objects.bulk_create([
            Product(
                id          = 1,
                intro       = "최고의 베스트셀러",
                title       = '100가지 장소의 보금자리',
                price       = "5800.00",
                description = "지금도 계속되고 있는 세계 각지로의 여행",
                image_url   = "https://wecode.com"
            ),
            Product(
                id          = 2,
                intro       = "최고의 베스트셀러",
                title       = '100가지 장소의 보금자리',
                price       = "5800.00",
                description = "지금도 계속되고 있는 세계 각지로의 여행",
                image_url   = "https://wecode.com"
            ),
            Product(
                id          = 3,
                intro       = "최고의 베스트셀러",
                title       = '100가지 장소의 보금자리',
                price       = "5800.00",
                description = "지금도 계속되고 있는 세계 각지로의 여행",
                image_url   = "https://wecode.com" 
            ),
            Product(
                id          = 4,
                intro       = "최고의 베스트셀러",
                title       = '100가지 장소의 보금자리',
                price       = "5800.00",
                description = "지금도 계속되고 있는 세계 각지로의 여행",
                image_url   = "https://wecode.com"    
            ),
            Product(
                id          = 5,
                intro       = "최고의 베스트셀러",
                title       = '100가지 장소의 보금자리',
                price       = "5800.00",
                description = "지금도 계속되고 있는 세계 각지로의 여행",
                image_url   = "https5://wecode.com"    
            )
        ])

        Author.objects.bulk_create([
            Author(
                id           = 1,
                name         = "이태훈",
                image_url    = "https://wecode.com",
                introduction = "최고의 베스트셀러 작가이다",
                product_id   = 1
            ),
            Author(
                id           = 2,
                name         = "김태훈",
                image_url    = "https://wecode.com",
                introduction = "최고의 베스트셀러 작가이다",
                product_id   = 2
            ),
            Author(
                id           = 3,
                name         = "삼태훈",
                image_url    = "https://wecode.com",
                introduction = "최고의 베스트셀러 작가이다",
                product_id   = 3
            ),
            Author(
                id           = 4,
                name         = "사태훈",
                image_url    = "https://wecode.com",
                introduction = "최고의 베스트셀러 작가이다",
                product_id   = 4
            ),
            Author(
                id           = 5,
                name         = "오태훈",
                image_url    = "https://wecode.com",
                introduction = "최고의 베스트셀러 작가이다",
                product_id   = 5
            )
            ])
        OrderStatus.objects.create(
            id = 1,
            name = '주문중'
        )

        PaymentType.objects.create(
            id =1,
            name = '카드결제'
        )

        ShoppingCart.objects.bulk_create([
            ShoppingCart(
                id              = 1,
                user_id         = 1,
                product_id      = 1,
                order_status_id = 1,
                payment_type_id = 1,
            ),
            ShoppingCart(
                id              = 2,
                user_id         = 1,
                product_id      = 2,
                order_status_id = 1,
                payment_type_id = 1,
            ),
            ShoppingCart(
                id              = 3,
                user_id         = 1,
                product_id      = 3,
                order_status_id = 1,
                payment_type_id = 1,
            ),
            ShoppingCart(
                id              = 4,
                user_id         = 1,
                product_id      = 4,
                order_status_id = 1,
                payment_type_id = 1,
            )
        ])

    def tearDown(self):
        User.objects.all().delete()
        Product.objects.all().delete()
        Author.objects.all().delete()
        ShoppingCart.objects.all().delete()

    def test_get_cart_succes(self):
        token    = jwt.encode({'id' : 1}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        header   = {"HTTP_Authorization" : token}
        response = self.client.get("/orders", **header)

        self.assertEqual(response.json(), {
            'cart_items': [
                {
                    'product_id'        : 1,
                    'user_id'           : 1,
                    'product_list'      : {
                        'product_title'     : '100가지 장소의 보금자리',
                        'product_image_url' : "https://wecode.com",
                        'product_price'     : 5800,
                        'author_name'       : '이태훈'
                    }
                },
                {
                    'product_id'        : 2,
                    'user_id'           : 1,
                    'product_list'      : {
                        'product_title'     : '100가지 장소의 보금자리',
                        'product_image_url' : "https://wecode.com",
                        'product_price'     : 5800,
                        'author_name'       : '김태훈'
                    }
                },
                {
                    'product_id'        : 3,
                    'user_id'           : 1,
                    'product_list'      : {
                        'product_title'     : '100가지 장소의 보금자리',
                        'product_image_url' : "https://wecode.com",
                        'product_price'     : 5800,
                        'author_name'       : '삼태훈'
                    }
                },
                    {
                    'product_id'        : 4,
                    'user_id'           : 1,
                    'product_list'      : {
                        'product_title'     : '100가지 장소의 보금자리',
                        'product_image_url' : "https://wecode.com",
                        'product_price'     : 5800,
                        'author_name'       : '사태훈'
                    }
                }
            ], 
            'total_product_price': {
                "product__price__sum": "23200.00",
            },
            'num_product': 4
        }
    )

        self.assertEqual(response.status_code, 200)

    def test_post_cart_success(self):
        token    = jwt.encode({'id' : 1}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        header   = {"HTTP_Authorization" : token}
        response = self.client.post('/orders', {'user_id': 1, 'product_id': 5, 'order_status_id': 1, 'payment_type_id':1},content_type='application/json', **header)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(),{'message' : 'SUCCESS'})

    def test_delete_cart_success(self):
        token    = jwt.encode({'id' : 1}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        header   = {"HTTP_Authorization" : token}
        response = self.client.delete('/orders/4', **header)

        self.assertEqual(response.status_code, 204)