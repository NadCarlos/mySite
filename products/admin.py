from django.contrib import admin
from django.utils.html import format_html
from products.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('name', 'price')

    search_fields = ('name', 'price', 'category__name')

    readonly_fields = ('name',)

    list_filter = ('category',)

    list_editable = ('price',)

    empty_value_display = "No data for this field yet"

    #exculde = ('name',)

    list_display = (
        'name', 
        'description', 
        'price',
        'category',
        'stock',
        'get_price_range',
        'get_total',
        'get_stock',
        )
    
    fieldsets = [
        (
            "Product Information",
            {
                "fields": ['name', 'price',],
            }
        ),
        (
            "More data",
            {
                "classes": ['collapse'],
                "fields": ['description', 'stock',],
            }
        )
    ]
    
    def get_total(self, obj):
        return obj.price * obj.stock
    
    def get_stock(self, obj):
        code = '#008000'
        low = '#FF0000'
        standard = '#FFD300'

        if obj.stock < 10:
            code = low
        if 10 < obj.stock < 100:
            code = standard

        return format_html(
            '<span style="color:{}">{}</span',
            code, obj.stock,
        )
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)