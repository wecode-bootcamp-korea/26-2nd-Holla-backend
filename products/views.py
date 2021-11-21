from django.views            import View
from django.http             import JsonResponse
from django.utils.dateformat import DateFormat

from .models                 import Product, Author
from users.models            import User
from reviews.models          import Review

class ProductView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id = product_id)
            author  = Author.objects.filter(product=product).first()
            
            result = [{
                "image_url"    : product.image_url,
                "intro"        : product.intro,
                "title"        : product.title,
                "price"        : product.price,
                "description"  : product.description,
                "author": {
                    "profile_url"  : author.image_url,
                    "name"         : author.name,
                    "introduction" : author.introduction
                }
            }]

            return JsonResponse({"product" : result}, status = 200)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "PRODUCT_DOES_NOT_EXIST"}, status = 404)