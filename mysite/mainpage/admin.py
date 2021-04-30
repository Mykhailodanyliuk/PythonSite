from django.contrib import admin
from  .models import Products
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'date')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Products,ProductsAdmin)