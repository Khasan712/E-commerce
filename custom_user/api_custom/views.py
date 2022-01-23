
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from custom_user.models import Custom_User

from .serializers import RegisterSerializer


@api_view(['POST'])
def register_user(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid:
            account = serializer.save()
            data['response'] = "Seccessfully registered"
            data['email'] = account.email
            data['username'] = account.username
            
        else:
            data = serializer.errors
        return Response(data)



