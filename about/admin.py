from django.contrib import admin
from .models import OurTeam, Adds_News, BrandImage, Brends
# Register your models here.

class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'date_modified', 'date_published')
    search_fields = ('name', 'last_name', 'about_self')
admin.site.register(OurTeam, OurTeamAdmin)

class Adds_NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_modified', 'date_published')
    search_fields = ('title', 'our_vision', 'our_mision')
admin.site.register(Adds_News, Adds_NewsAdmin)

class BrandImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'date_modified', 'date_published']
admin.site.register(BrandImage, BrandImageAdmin)


class BrendsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_modified', 'date_published')
    search_fields = ('title', 'description')
admin.site.register(Brends, BrendsAdmin)