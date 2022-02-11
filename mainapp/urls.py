from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:main_slug>', views.products_list, name='products_list'),
    path('product/<int:pk>/view', views.product_view, name='product_view'),
    path('search', views.search, name='search'),
]

