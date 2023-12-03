from django.shortcuts import render
from requests import Response
from TraineerbookApp.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from TraineerbookApp.serializer import *

# Create your views here.


class getProductsApiViewSet(ModelViewSet):
  http_method_names = ['get']
  
  def get_queryset(self):
    products = Product.objects.all()
    serializer = GetProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class getProductDetailApiViewSet(ModelViewSet):
  http_method_names = ['get']

  def get_queryset(self,request,pk):
    product = Product.objects.get(id=pk)
    serializer = GetProductSerializer(product, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)