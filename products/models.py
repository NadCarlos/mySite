from django.contrib import admin
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    @admin.display(description="Price Range")
    def get_price_range(self):
        if self.price > 100:
            return 'Alto'
        if 50 < self.price < 100:
            return 'Medio'
        else:
            return 'Bajo'

    def __str__(self):
        return self.name