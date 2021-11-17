from django.db import models

class ShoppingCart(models.Model):
    user         = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product      = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)
    payment_type = models.ForeignKey('PaymentType', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'shopping_carts'

class OrderStatus(models.Model):
    name  = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'order_status'

class PaymentType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'payment_types'        