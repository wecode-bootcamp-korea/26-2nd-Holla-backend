from django.http import response
from django.test import TestCase, Client, client

from orders.models   import ShoppingCart
from products.models import Product, Author
from users.models    import User

class CartGetTest(TestCase):
    def setup(self):
        self.client = Client()

        User.objects.create(
            id = 1,
            email = 'qudans@naver.com',    
            name  = '김코드',  
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

        ShoppingCart.objects.bulk_create([
            ShoppingCart(
                user_id = 1,
                roduct_id =1,
                order_status_id =1,
                payment_type_id =1,
            ),
            ShoppingCart(
                user_id = 1,
                product_id =2,
                order_status_id =1,
                payment_type_id =1,
            ),
            ShoppingCart(
                user_id = 1,
                product_id =3,
                order_status_id =1,
                payment_type_id =1,
            ),
            ShoppingCart(
                user_id = 1,
                product_id =4,
                order_status_id =1,
                payment_type_id =1,
            )
        ])

def tearDown(self):
        User.objects.all().delete()
        Product.objects.all().delete()
        Author.objects.all().delete()
        ShoppingCart.objects.all().delete()

def test_get_cart_succes(self):
    response = self.client.get('/orders/cart')

    self.assertEqual(response.json(),({
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
            }], 
        'total_product_price': 23200,
        'total_product': 4
        }
        ))

    self.assertEqual(response.status_code, 200)

def test_post_cart_succes(self):
    shoppingCart = {
        'user_id'    : 1,
        'product_id' : 5
    }

    response = self.client.post('/orders/cart', json.dumps(shoppingCart), content_type='application/json')

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json(),
        {
            'message' : 'SUCCESS'
        }
    )