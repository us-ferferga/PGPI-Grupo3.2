import datetime
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from TraineerbookApp.models import Activity, Product
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from TraineerbookApp.serializer import *
from datetime import datetime as dt
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

# views.py
from .models import Reservation

class ShoppingCartGetView(APIView):
    def get(self, request):
        # Recupera y devuelve los productos en la cesta del usuario
        cart_products = request.session.get('cart_products', [])
        serializer = CartProductSerializer(cart_products, many=True)

        reservations = []
        for item in cart_products:
            product_id = item['product_id']
            quantity = item['quantity']

            # Aquí asumimos que ya has autenticado al usuario, y obtenemos el usuario actual
            user = request.user if request.user.is_authenticated else None

            # Método de pago predeterminado en caso de que no se proporcione
            buy_method = 'online'

            # Crea una reserva para cada producto en el carrito
            reservation = Reservation.objects.create(
                user=user,
                product_id=product_id,
                buy_date=datetime.datetime.now(),  # Utiliza la fecha y hora actual
                buy_method=buy_method,
            )
            reservations.append(reservation)

        # Limpia el carrito después de crear las reservas
        request.session['cart_products'] = []

        # Devuelve los productos del carrito y las reservas creadas
        return Response({'cart_products': serializer.data, 'reservations': ReservationSerializer(reservations, many=True).data})


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



class PaymentProcessView(APIView):
    def post(self, request):
        # Recupera y devuelve los productos en la cesta del usuario
        cart_products = request.session.get('cart_products', [])

        # Lógica para procesar el pago y obtener los productos comprados
        # En este ejemplo, simplemente obtenemos la lista de productos del carrito
        products_comprados = cart_products

        # Crear reservas para los productos comprados
        reservations = []
        for item in products_comprados:
            product_id = item['product_id']
            quantity = item['quantity']

            # Verifica si el producto existe
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

            # Crea una reserva para el producto comprado
            reservation_data = {
                'user': request.user,  # Ajusta esto según cómo manejes a los usuarios en tu aplicación
                'product': product,
                'quantity': quantity,
                'buy_date': datetime.today(),  # O ajusta esto según sea necesario
                'buy_method': 'online',  # Ajusta esto según tu lógica de compra
            }
            serializer = ReservationSerializer(data=reservation_data)
            if serializer.is_valid():
                serializer.save()
                reservations.append(serializer.data)

        # Limpia el carrito después de procesar el pago
        del request.session['cart_products']

        return Response({'reservations': reservations}, status=status.HTTP_201_CREATED)

