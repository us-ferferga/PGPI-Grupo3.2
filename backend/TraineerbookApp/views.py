from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from TraineerbookApp.models import Activity, Product
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from TraineerbookApp.serializer import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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

        # Create a dictionary to store aggregated quantities and prices for each product
        product_aggregation = {}

        # Aggregate quantities and prices for each product
        for item in cart_products:
            try:
                product = Product.objects.get(id=item['product_id'])
                quantity = item['quantity']
                price = product.price * quantity

                if product.id not in product_aggregation:
                    product_aggregation[product.id] = {
                        'activity_description': product.activity.description,
                        'product_hour_init': product.product_hour_init,
                        'product_hour_fin': product.product_hour_fin,
                        'quantity': quantity,
                        'total_price': price,
                    }
                else:
                    product_aggregation[product.id]['quantity'] += quantity
                    product_aggregation[product.id]['total_price'] += price

            except Product.DoesNotExist:
                # Handle the case where the product no longer exists
                pass

        # Convert the aggregated data to a list for serialization
        aggregated_data = list(product_aggregation.values())

        # Serialize using GetProductSerializer and the aggregated data
        serializer = GetProductSerializer(data=aggregated_data, many=True)
        serializer.is_valid()

        return Response(serializer.data)



@swagger_auto_schema(
    query_serializer=CartProductSerializer,  # Especifica el serializador para parámetros de consulta
)
class ShoppingCartPutView(APIView):
    serializer_class = CartProductSerializer

    def put(self, request, product_id, quantity):
        # Obtén el serializer con los datos de la solicitud
        serializer = self.serializer_class(data={'product_id': product_id, 'quantity': quantity})

        # Verifica la validez del serializer
        if serializer.is_valid():
            # Accede a la cantidad validada
            quantity = serializer.validated_data['quantity']

            # Resto del código para manejar el carrito
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            cart_products = request.session.get('cart_products', [])

            for item in cart_products:
                if item['product_id'] == int(product_id):
                    item['quantity'] += quantity
                    break
            else:
                cart_products.append({'product_id': int(product_id), 'quantity': quantity})

            request.session['cart_products'] = cart_products

            return Response(status=status.HTTP_201_CREATED)
        else:
            # Si el serializer no es válido, devuelve los errores
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

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