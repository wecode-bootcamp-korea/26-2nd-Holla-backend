import json,requests

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Sum

from orders.models   import ShoppingCart
from products.models import Author
from core.utils      import login_decorator

class CartGetView(View):
    @login_decorator
    def get(self, request):
        try:
            carts = ShoppingCart.objects.filter(user_id = request.user.id)
            cart_items = [{
                "product_id"   : shoppingcart.product.id,
                "user_id"      : shoppingcart.user.id,
                "product_list" : {
                    "product_title"     : shoppingcart.product.title,
                    "product_image_url" : shoppingcart.product.image_url,
                    "product_price"     : int(shoppingcart.product.price),
                    "author_name"       : Author.objects.get(product_id=shoppingcart.product.id).name,
                }
            } for shoppingcart in carts]

            total_product_price = carts.aggregate(Sum('product__price'))
            
            result = {
            "cart_items"          : cart_items,
            "total_product_price" : total_product_price,
            "num_product"         : len(carts)
            }

            return JsonResponse(result, status=200)

        except ShoppingCart.DoesNotExist:
            return JsonResponse({"message" : "SHOPPINGCART_DOES_NOT_EXIST"}, status = 400)
        
class CartPostView(View):
    @login_decorator
    def post(self, request):
        try:
            data       = json.loads(request.body)
            product_id = data['product_id']

            ShoppingCart.objects.create(
                product_id = product_id,
                user_id    = request.user.id,
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

class CartDeleteView(View):
    login_decorator
    def delete(self, request, product_id):
        ShoppingCart.objects.filter(user_id = request.user.id, product_id = product_id).delete()

        return JsonResponse({"message" : "SUCCESS"}, status=204)
