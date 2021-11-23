from django.urls import path, include

from products.views import MainTotalView

urlpatterns = [
    path('', MainTotalView.as_view()),
    path('products', include('products.urls')),
    path('users', include('users.urls')),
]