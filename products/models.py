from django.db import models

class Product(models.Model):
    intro       = models.CharField(max_length=200)
    title       = models.CharField(max_length=100)
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=2000)
    image_url   = models.CharField(max_length=2000)
    genre       = models.CharField(max_length=100, default='')
    deleted_at  = models.DateTimeField(null=True)

    class Meta:
        db_table = 'products'

class Author(models.Model):
    name         = models.CharField(max_length=30)
    image_url    = models.CharField(max_length=2000)
    introduction = models.CharField(max_length=2000)
    product      = models.ForeignKey('Product',on_delete=models.CASCADE)

    class Meta:
        db_table = 'authors'