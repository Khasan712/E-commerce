from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('section/product/<int:pk>', views.products_list, name='products_list'),
    path('section/product/<int:pk>/view', views.product_view, name='product_view'),
    path('search', views.search, name='search'),
]

