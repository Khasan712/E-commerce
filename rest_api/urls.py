from unicodedata import name
from xml.etree.ElementInclude import include
from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register('', views.ProductViewset, basename='product')
router.register('main_category', views.MainCategoryViewset, basename='main_category')
router.register('', views.ProductCategoriesViewset, basename='category_product')
router.register('', views.SizesProductsViewset, basename='size_product')
router.register('', views.ColorsProductsViewset, basename='color_product')
router.register('', views.ImageProductViewset, basename='image_product')
router.register('', views.ProductViewset, basename='product')


urlpatterns = [
    path('', include(router.urls))
]
