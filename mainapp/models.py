from django.db import models
from django.db.models.deletion import CASCADE
# from djmoney.models.fields import MoneyField
from colorfield.fields import ColorField
from taggit.managers import TaggableManager
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from config import settings


# Create your models here.

class MainCategory(models.Model):
    category = models.CharField(max_length=220, blank=True)
    main_slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.category
    
    def get_main_category_products_count(self):
        return self.main_category.count()



class ProductCategories(models.Model):
    title = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title
    
    def get_category_products_count(self):
        return self.product_category.count()




class SizesProducts(models.Model):
    sizes = models.CharField(max_length=220, blank=True)

    def get_size_products_count(self):
        return self.size.count()
    
    def __str__(self):
        return self.sizes


# class ColorsProducts(models.Model):
#     colors =ColorField(max_length=220, blank=True)

#     def get_colors_products_count(self):
#         return self.color.count()

#     def __str__(self):
#         return self.colors

class ColorsProducts(models.Model):
    colors =models.CharField(max_length=220, blank=True)

    def get_colors_products_count(self):
        return self.color.count()

    def __str__(self):
        return self.colors


class ImageProduct(models.Model):
    image = models.FileField(upload_to='product/image', blank=True)

    def __str__(self):
        return str(self.image)




class Product(models.Model):
    TOP_NEW_CHOICES = (
        ('',''),
        ('top','top'),
        ('new','new'),
    )

    QTY_CHOICES = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    )
    image = models.ManyToManyField(ImageProduct, blank=True)
    title = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    main_category = models.ManyToManyField(MainCategory, blank=True, related_name='main_category')
    product_category = models.ManyToManyField(ProductCategories, blank=True, related_name='product_category')
    price = models.FloatField(blank=True, null=True)
    # print(type(price))
    color = models.ManyToManyField(ColorsProducts, blank=True, related_name='color')
    size = models.ManyToManyField(SizesProducts, blank=True, related_name='size')
    tag = TaggableManager(blank=True)
    discount = models.DecimalField(decimal_places=2, max_digits=14, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation', blank=True)
    top_or_new = models.CharField(max_length=3, choices=TOP_NEW_CHOICES, default='', blank=True)

    qty_product = models.PositiveIntegerField(default='1', blank=True, null=True)

    product_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'product_user',
        blank=True, null=True
    )

    def __str__(self):
        return self.title



