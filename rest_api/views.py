from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from mainapp.models import Product, MainCategory, ProductCategories, SizesProducts, ColorsProducts, ImageProduct
from .serializers import ProductsSerializers, MainCategorySerializers, ProductCategoriesSerializers, SizesProductsSerializers, ColorsProductsSerializers, ImageProductSerializers



class MainCategoryViewset(viewsets.ModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializers

class ProductCategoriesViewset(viewsets.ModelViewSet):
    queryset = ProductCategories.objects.all()
    serializer_class = ProductCategoriesSerializers

class SizesProductsViewset(viewsets.ModelViewSet):
    queryset = SizesProducts.objects.all()
    serializer_class = SizesProductsSerializers

class ColorsProductsViewset(viewsets.ModelViewSet):
    queryset = ColorsProducts.objects.all()
    serializer_class = ColorsProductsSerializers

class ImageProductViewset(viewsets.ModelViewSet):
    queryset = ImageProduct.objects.all()
    serializer_class = ImageProductSerializers

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializers



