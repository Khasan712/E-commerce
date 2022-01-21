from django.contrib import admin

# Register your models here.

from  .models import *

class BlogVideosAdmin(admin.ModelAdmin):
    list_display = ['id', 'video', 'date_modified', 'date_published']
    search_fields = ('video', 'date_modified', 'date_published')
admin.site.register(BlogVideos, BlogVideosAdmin)

class BlogImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'date_modified', 'date_published']
    search_fields = ('image', 'date_modified', 'date_published')
admin.site.register(BlogImages, BlogImagesAdmin)

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'date_modified', 'date_published']
    search_fields = ('category', 'date_modified', 'date_published')
admin.site.register(BlogCategory, BlogCategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_author', 'date_modified', 'date_published')
    search_fields = ('blog_author', 'title', 'text', 'tags', 'blog_category', 'date_modified', 'date_published')
    list_filter = ('tags', 'blog_category')
admin.site.register(Blog, BlogAdmin)

class BlogCommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'comment_user', 'name', 'email', 'parent', 'date_modified', 'date_published']
    search_fields = ('comment_user', 'name', 'email', 'message', 'parent', 'date_modified', 'date_published')
admin.site.register(BlogComments, BlogCommentsAdmin)

