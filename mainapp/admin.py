from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import *

class ProductAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        # image_url = ob.image.all.first.image.url
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.all))
    image_tag.short_description = 'Image'
    list_display = ['id', 'product_user', 'date_modified', 'date_published', 'image_tag']
    list_display_links = ['id', 'product_user']
    readonly_fields = ['image_tag']
    list_filter = ('product_user', 'main_category', 'product_category', 'date_modified', 'date_published')
    list_per_page = 15
    search_fields = ('discount', 'tag', 'price', 'size', 'main_category', 'product_category', 'description', 'title', 'product_user', 'date_modified', 'date_published',)


admin.site.register(Product, ProductAdmin)

@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'main_slug']
    prepopulated_fields = {'main_slug':('category',)}

admin.site.register(ProductCategories)

class ImageProductAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    list_display = ['image_tag',]
    readonly_fields = ['image_tag']

admin.site.register(ImageProduct, ImageProductAdmin)




admin.site.register(SizesProducts)
admin.site.register(ColorsProducts)