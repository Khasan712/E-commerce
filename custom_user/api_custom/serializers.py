from asyncio.format_helpers import extract_stack
from distutils.file_util import write_file
from tkinter.ttk import Style
from rest_framework import serializers

from custom_user.models import Custom_User

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Custom_User
        fileds = ['email', 'username', 'password', 'password2']
        extract_kwargs = {
            'password' : {'write_only':True}
        }
    
    def save(self):
        account = Custom_User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({
                'password' : 'Passwords must match.'
            })
        account.set_password(password)
        account.save()
        return account
        
        
        