import json

from django.views     import View
from django.http      import JsonResponse

from orders.models   import ShoppingCart

class CartListView(View):
    def get(self, request):
        try:
            carts= ShoppingCart.objects.filter(user_id = request.user.id)
            cart_items = [{
                "shoppingcart_id"   : shoppingcart.id,
                "product_id"        : shoppingcart.product.id,
                "user_id"           : shoppingcart.user.id,
                "product_title"     : shoppingcart.product.title,
                "product_image_url" : shoppingcart.product.image_url,
                "product_price"     : int(shoppingcart.product.price),
                "author_name"       : shoppingcart.product.author_set.name,
            }for shoppingcart in carts]
        
            total_product_price = sum([int(shoppingcart.product.price) for shoppingcart in carts])
            
            return JsonResponse({"cart_items" : cart_items, "total_product_price" :total_product_price}, status=200)

        except ShoppingCart.DoesNotExist:
            return JsonResponse({"message" : "SHOPPINGCART_DOES_NOT_EXIST"}, status = 400)
        

    def post(self, request):
        try:
            data              = json.loads(request.body)
            product_id        = data['product_id']
            user_id           = data['user_id']

            ShoppingCart.objects.create(
                product_id        = product_id,
                user_id           = user_id,
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

    def delete(self, request, id):
        ShoppingCart.objects.filter(user_id = request.user.id, id = id).delete()

        return JsonResponse({"message" : "SUCCESS"}, status=204)