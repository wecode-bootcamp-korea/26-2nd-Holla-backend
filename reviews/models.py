from django.db import models
from core.models    import TimeStampModel

class Review(TimeStampModel):
    user           = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product        = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    text           = models.CharField(max_length=2000)
    rating         = models.DecimalField(max_digits=2, decimal_places=1)
    
    class Meta:
        db_table = 'reviews'