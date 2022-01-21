from django.db import models
from phone_field import PhoneField

# Create your models here.

class AddsContact(models.Model):
    image = models.ImageField(upload_to='contact/add\'s')
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

class ContactInfo(models.Model):
    text = models.TextField(blank=True)
    address = models.TextField(blank=True)        
    comp_tel = PhoneField(blank=True)
    comp_email = models.EmailField(max_length=250, blank=True)
    weekly = models.CharField(max_length=250, blank=True)
    weekly_time = models.CharField(max_length=250, blank=True)
    short_day = models.CharField(max_length=250, blank=True)
    short_day_time = models.CharField(max_length=250, blank=True)

class ContactUser(models.Model):
    name = models.CharField(max_length=250, blank=True)
    email = models.ImageField(max_length=250, blank=True)
    phone = PhoneField(blank=True)
    subject = models.CharField(max_length=250, blank=True)
    message = models.TextField(blank=True)

class OurBranch(models.Model):
    image = models.ImageField(upload_to='contact/branch_image')
    comp_address = models.CharField(max_length=300, blank=True)
    comp_street = models.CharField(max_length=300, blank=True)
    phone = PhoneField(blank=True)
    weekly = models.CharField(max_length=250, blank=True)
    short_day = models.CharField(max_length=250, blank=True)
    comp_map = models.URLField(blank=True)



        
