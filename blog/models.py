from os import read
from django.db import models
from django.db.models.fields.files import FileField
from django.core.validators import FileExtensionValidator
from taggit.managers import TaggableManager
from django_resized import ResizedImageField
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.
from config import settings


class BlogVideos(models.Model):
    video = models.FileField(
        upload_to='media/blog/videos',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
        blank=True
    )
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.video)

class BlogImages(models.Model):
    image = ResizedImageField(size=[1000, 1000], upload_to='media/blog/imahes', force_format='png', quality=75, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def get_first_image(self):
        return self.images.first()



class BlogCategory(models.Model):
    category = models.CharField(max_length=200, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.category
    
    def get_category_count(self):
        return self.blog_category.count()


class Blog(models.Model):
    images = models.ManyToManyField('BlogImages', blank=True, related_name='images')
    video = models.ManyToManyField('BlogVideos', blank=True)
    blog_author = models.ForeignKey(settings.AUTH_USER_MODEL, default='admin', on_delete=models.CASCADE,  related_name = 'blog_author',)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    title = models.CharField(max_length=500)
    text = models.TextField()
    blog_category = models.ManyToManyField('BlogCategory', related_name='blog_category')
    tags = TaggableManager(blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title
    
    def get_all_tags(self):
        pass

    def get_comments_count(self):
        return self.comments.count()
    
    
            
    
    

class BlogComments(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    comment_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'comment_author',
        null=True
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')

    def __str__(self):
        return '%s - %s' % (self.blog.title, self.name)

#     # def children(self):
#     #     return BlogComments.objects.filter(parent=self)

#     # @property
#     # def is_parent(self):
#     #     if self.parent is not None:
#     #         return False
#     #     return True

#     class Meta:
#         ordering = ['date_published']
#         verbose_name = "Blog Comment"
#         verbose_name_plural = "Blog Comments"