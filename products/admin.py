""" Imports """
from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    """ Product admin model"""
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image_url'
    )


class CategoryAdmin(admin.ModelAdmin):
    """ Category admin model """
    list_display = (
        'friendly_name',
        'name'
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)
