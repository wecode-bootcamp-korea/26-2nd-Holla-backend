from django.urls import path

from products.views import ProductView
from reviews.views  import ReviewView

app_name = 'products'
urlpatterns = [
    path('/<int:product_id>', ProductView.as_view()),
    path('/<int:product_id>', ReviewView.as_view()),
]