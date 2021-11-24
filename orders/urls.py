from django.urls import path

from orders.views import CartGetView, CartPostView, CartDeleteView

app_name = 'orders'
urlpatterns = [
    path('/cart', CartGetView.as_view()),
]