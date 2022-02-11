import django_filters


from .models import Product


class ProductItemsFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['product_category']