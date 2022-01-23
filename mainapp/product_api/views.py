from itertools import product
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from mainapp.models import (
    MainCategory,
    ProductCategories,
    ImageProduct,
    ColorsProducts,
    SizesProducts,
    Product
)
from .serializers import ProductsSerializers
from custom_user.models import Custom_User

from mainapp.product_api import serializers


@api_view(['GET',])
def api_product_view(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductsSerializers(product)
        return Response(serializer.data)


@api_view(['PUT',])
def api_product_update(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ProductsSerializers(product, data=request.data)
        data = {}
        if serializer.is_valid:
            serializer.save()
            data["success"] = "Updated successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def api_product_delete(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        operation = product.delete()
        data = {}
        if operation:
            data["success"] = "Deleted successful"
        else:
            data["False"] = "Something wrong"
        return Response(data=data)


@api_view(['POST',])
def api_product_create(request):
    product_user = Custom_User.objects.get(id=1)
    if request.method == 'POST':
        serializer = ProductsSerializers(product_user, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = {}
        data["False"] = "Aomething wrong"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        


















