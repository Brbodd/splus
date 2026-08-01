from django.contrib import admin
from .models import Product, ProductCategory

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ['name']
    }

    list_display = ["__str__", "category", "price"]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)