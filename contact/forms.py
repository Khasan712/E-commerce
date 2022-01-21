from django import forms
from django.db.models import fields
from .models import *


class ContactUserForm(forms.ModelForm):
    class Meta:
        model = ContactUser
        fields = '__all__'
        