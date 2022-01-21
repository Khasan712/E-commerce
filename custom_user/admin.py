from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Custom_User
# Register your models here.



class Custom_UserAdmin(UserAdmin):
    list_filter = ()
    list_display = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'date_joined', 'date_modified', 'date_published', 'is_superuser', 'is_staff', 'is_active')
    search_fields = ('username',)
    list_display_links = ['id', 'username']
admin.site.register(Custom_User, Custom_UserAdmin)
