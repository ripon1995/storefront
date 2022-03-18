from encodings import search_function
from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin) :
    list_display = ['title']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin) :
    list_display = ['id','title','unit_price','inventory_status']
    list_editable = ['unit_price']
    list_per_page = 10

    def inventory_status(self,product) :
        if product.inventory < 10 :
            return 'Low'
        return 'OK'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin) :
    list_display = ['first_name','last_name','membership']
    list_editable = ['membership']
    list_per_page = 10
    search_fields = ['first_name','last_name']

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin) :
    list_display = ['id','placed_at','customer']
