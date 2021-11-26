from django.views            import View
from django.http             import JsonResponse

from .models                 import Product, Author
from users.models            import User
from reviews.models          import Review
from core.utils              import login_decorator

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

class MainTotalView(View):
    @login_decorator
    def get(self, request):
        products = Product.objects.filter(shoppinghistory__user__id=request.user.id)
        if not products:
            books_info = [{
                "id"             : product.id,
                "product_images" : product.image_url,
                "intro"          : product.intro 
            } for product in Product.objects.order_by("?")[:10]]
        
        elif products:
            genre_list = [product.genre for product in products]
            like_genre = max(set(genre_list), key=genre_list.count)
            books_info = [{
                "id"             : product.id,
                "product_images" : product.image_url,
                "intro"          : product.intro 
            } for product in Product.objects.filter(genre=like_genre)[:10]]
        
        reviews_info = [{
            "id"             : review.product.id,
            "product_images" : review.product.image_url,
            "text"           : review.text,
            "name"           : review.user.name
        } for review in Review.objects.order_by("created_at")[:6]]
        
        month_info = [{
            "id"             : product.id,
            "product_images" : product.image_url,
            "title"          : product.title,
            "author"         : Author.objects.get(product_id=product.id).name,
            "author_images"  : Author.objects.get(product_id=product.id).image_url
        } for product in Product.objects.order_by("?")[:10]]
        
        results = {
            "name"              : request.user.name, 
            "recommend_books"   : books_info,
            "realtime_reviews"  : reviews_info,
            "book_of_the_month" : month_info
        }

        return JsonResponse({
            "message" : "SUCCESS", "results" : results}, status = 200)
