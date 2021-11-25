import json

from django.http             import JsonResponse
from django.views            import View
from django.db.models        import Avg
from django.utils.dateformat import DateFormat

from core.utils              import login_decorator
from .models                 import Review

class ReviewView(View):
    def get(self, request, product_id):
        try:
            reviews       = Review.objects.filter(product_id=product_id)
            avg_rating    = reviews.aggregate(Avg('rating'))['rating__avg']
            total_reviews = len(reviews)

            result = {
                "total_reviews" : total_reviews,
                "avg_rating"    : round(avg_rating, 1) if avg_rating != None else 0,
                "reviews"       : [{
                    "id"   : review.id,
                    "name" : review.user.name,
                    "date" : DateFormat(review.created_at).format('Y.m.d h:m'),
                    "text" : review.text,
                } for review in reviews]
            }

            return JsonResponse({"result" : result}, status = 200)
    
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 401)

    @login_decorator
    def post(self, request, product_id):
        try:
            data    = json.loads(request.body)
            rating  = data["rating"]
            text    = data["text"]
            user    = request.user
            product = product_id

            Review.objects.create(
                rating     = rating,
                text       = text,
                user_id    = user,
                product_id = product
            )

            return JsonResponse({"message" : "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 401)

    @login_decorator
    def delete(self, request, product_id):
        user    = request.user.id
        product = product_id
        Review.objects.get(user_id=user, product_id=product).delete()
        
        return JsonResponse({"message" : "SUCCESS"}, status = 200)