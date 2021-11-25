from django.urls import path

from products.views import ProductView

app_name = 'products'
urlpatterns = [
    path('/<int:product_id>', ProductView.as_view()),
]