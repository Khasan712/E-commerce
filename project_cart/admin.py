from django.contrib import admin
from .models import *
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart_id', 'date_added')
admin.site.register(Cart, CartAdmin)

class CartItemAdin(admin.ModelAdmin):
    list_display = ('id', 'product', 'cart', 'is_active')
admin.site.register(CartItem, CartItemAdin)