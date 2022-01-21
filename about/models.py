from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils.html import format_html
from django_resized import ResizedImageField



class OurTeam(models.Model):
    image = ResizedImageField(size=[400, 600], upload_to='media/about/our-team/', force_format='png', quality=75)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    staff = models.CharField(max_length=150)
    about_self = models.CharField(max_length=400)
    facebook_link = models.URLField(max_length=200)
    twetter_link = models.URLField(max_length=200)
    instagram_link = models.URLField(max_length=200)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Our Team"

    def team_member_count(self):
        return self.count()


class Adds_News(models.Model):
    image = models.ImageField(upload_to='media/about/adds/')
    center = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    our_vision = models.CharField(max_length=100)
    our_vision_full = models.TextField()
    our_mision = models.CharField(max_length=100)
    our_mision_full = models.TextField()
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Add News"

class BrandImage(models.Model):
    image = models.ImageField(upload_to='media/about/brands/')
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Brand Icons"
        get_latest_by = ['-date_modified']

class Brends(models.Model):
    title = models.CharField(max_length=350)
    description = models.CharField(max_length=350)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ManyToManyField(
        'BrandImage', blank=True, related_name='brand_icons'
    )

    class Meta:
        verbose_name_plural = "Centre Brand"