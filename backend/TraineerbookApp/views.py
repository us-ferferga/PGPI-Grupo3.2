from django.shortcuts import get_object_or_404, render
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

class ShoppingCartGetView(APIView):
    def get(self, request):
        # Recupera y devuelve los productos en la cesta del usuario
        cart_products = request.session.get('cart_products', [])
        serializer = CartProductSerializer(cart_products, many=True)
        return Response(serializer.data)

class ShoppingCartPutView(APIView):
    def put(self, request, product_id):
        # Obtén la cantidad del request.data
        quantity = request.data.get('quantity', 1)  # Valor predeterminado de 1 si no se proporciona

        # Verifica si el producto existe
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Obtiene o inicializa el carrito en la sesión
        cart_products = request.session.get('cart_products', [])

        # Intenta encontrar el producto en el carrito
        for item in cart_products:
            if item['product_id'] == int(product_id):
                item['quantity'] += quantity
                break
        else:
            # Si el producto no estaba en el carrito, agrégalo
            cart_products.append({'product_id': int(product_id), 'quantity': quantity})

        request.session['cart_products'] = cart_products

        return Response(status=status.HTTP_201_CREATED)


class ShoppingCartDeleteView(APIView):
    def delete(self, request, product_id):
        # Elimina un producto de la cesta
        cart_products = request.session.get('cart_products', [])

        # Busca y elimina el producto de la cesta
        for product in cart_products:
            if product['product_id'] == product_id:
                cart_products.remove(product)
                request.session['cart_products'] = cart_products
                return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)