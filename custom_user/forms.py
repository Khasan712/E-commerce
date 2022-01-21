from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Custom_User
from django import forms
from mainapp.models import Product
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox

class Custom_UsereForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Custom_User
        fields = ('username', 'email')

class EditCustom_UserForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = Custom_User
        fields = ['first_name', 'last_name', 'username', 'email', 'img', 'back_img', 'bio', 'tel', 'address', 'website']


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'main_category', 'product_category', 'image', 'description', 'price', 'color', 'size', 'tag', 'discount')