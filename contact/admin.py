from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(AddsContact)
admin.site.register(ContactInfo)
admin.site.register(ContactUser)
admin.site.register(OurBranch)