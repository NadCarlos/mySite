from django.contrib import admin
from products.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']