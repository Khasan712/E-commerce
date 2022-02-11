from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('cart/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('cart/delete/<int:product_id>/', views.delete_cart_item, name='delete_cart_item'),

    path('checkout/', views.checkout, name="checkout"),
]
