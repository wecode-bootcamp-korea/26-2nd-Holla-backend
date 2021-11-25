from django.urls import path

from orders.views import CartView

app_name = 'orders'
urlpatterns = [
    path('', CartView.as_view()),
    path('/<int:product_id>', CartView.as_view())
]