from django.contrib import admin
from products.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('name', 'price')

    search_fields = ('name', 'price', 'category__name')

    list_filter = ('category',)

    list_editable = ('price',)

    empty_value_display = "No data for this field yet"

    #exculde = ('name',)

    list_display = (
        'name', 
        'description', 
        'price',
        'category',
        )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)