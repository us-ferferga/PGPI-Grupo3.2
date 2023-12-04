from django.shortcuts import render
from rest_framework.response import Response
from TraineerbookApp.models import Activity, Product
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from TraineerbookApp.serializer import *

from rest_framework.views import APIView

# Create your views here.

"""GET devuelve listado de productos al completo FUNCIONAL"""
class getProductsApiViewSet(ModelViewSet):
    http_method_names = ['get']

    serializer_class = GetProductSerializer2
    queryset = Product.objects.all()

"""GET devuelve listado de productos segun el id sea igual a la actividad del producto FUNCIONAL"""

class getProductDetailApiViewSet(ModelViewSet):
  serializer_class = GetProductSerializer2
  
  def get_queryset(self):
      
      pk = self.kwargs.get('pk')
      queryset = Product.objects.all().filter(activity=pk)
      return queryset
      

"""GET devuelve listado de actividades al completo FUNCIONAL"""
class getActivityApiViewSet(ModelViewSet):
    http_method_names = ['get']

    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
