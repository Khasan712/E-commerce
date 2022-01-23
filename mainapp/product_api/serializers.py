from dataclasses import field
from rest_framework import serializers

from mainapp.models import Product, MainCategory, ProductCategories, SizesProducts, ColorsProducts, ImageProduct


class MainCategorySerializers(serializers.ModelSerializer):
    # MainCategory_user = serializers.CharField()
    class Meta:
        model = MainCategory
        fields = '__all__'


class ProductCategoriesSerializers(serializers.ModelSerializer):
    # ProductCategories_user = serializers.CharField()
    class Meta:
        model = ProductCategories
        fields = '__all__'

class SizesProductsSerializers(serializers.ModelSerializer):
    # SizesProducts_user = serializers.CharField()
    class Meta:
        model = SizesProducts
        fields = '__all__'

class ColorsProductsSerializers(serializers.ModelSerializer):
    # ColorsProducts_user = serializers.CharField()
    class Meta:
        model = ColorsProducts
        fields = '__all__'

class ImageProductSerializers(serializers.ModelSerializer):
    # ImageProduct_user = serializers.CharField()
    class Meta:
        model = ImageProduct
        fields = '__all__'


class ProductsSerializers(serializers.ModelSerializer):
    product_user = serializers.CharField()
    class Meta:
        model = Product
        fields = '__all__'