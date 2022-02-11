


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from contact.models import ContactUser
from .serializers import ContactUserSerializer


@api_view(['POST',])
def create_api_contact(request):
    serializer = ContactUserSerializer()
    if request.method == 'POST':
        serializer = ContactUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = {}
        data["False"] = "Anything is wrong"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
def get_api_contact(request, pk):
    try:
        contact = ContactUser.objects.get(id=pk)
    except ContactUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ContactUserSerializer(contact)
        return Response(serializer.data)



@api_view(['PUT',])
def put_api_contact(request, pk):
    try:
        contact = ContactUser.objects.get(id=pk)
    except ContactUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ContactUserSerializer(contact, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            data["success"] = "Updated successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
def delete_api_contact(request, pk):
    try:
        contact = ContactUser.objects.get(id=pk)
    except ContactUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        operation = contact.delete()
        data = {}
        if operation:
            data["success"] = "Deleted successful"
        else:
            data['false'] = "Wrong paremetrs"
        return Response(data=data)








