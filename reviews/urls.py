from django.urls import path

from reviews.views import ReviewView

app_name = 'reviews'
urlpatterns = [
    path('/<int:product_id>', ReviewView.as_view())
]