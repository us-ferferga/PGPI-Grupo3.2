from django.shortcuts import render
from rest_framework.response import Response
from TraineerbookApp.models import Activity, Product
from rest_framework.viewsets import ModelViewSet
from TraineerbookApp.serializer import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.openapi import Response as SwaggerResponse
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from TraineerbookApp.serializer import UserSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated 

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

class RegisterUserView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={200: 'OK', 400: 'Bad Request'},
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Crear el usuario y establecer la contraseña sin guardarlo inmediatamente
            user = serializer.save()

            # Establecer la contraseña y guardar el usuario
            user.set_password(request.data.get('password'))
            user.save()

            # Iniciar sesión automáticamente después del registro
            login(request, user)

            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={200: 'OK', 400: 'Bad Request'},
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                # Generar o recuperar el token del usuario
                token, created = Token.objects.get_or_create(user=user)

                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Obtener el token asociado al usuario actual
        try:
            token = Token.objects.get(user=request.user)
        except Token.DoesNotExist:
            # Si el token no existe, la sesión ya se considera cerrada
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_400_BAD_REQUEST)

        # Eliminar el token de autenticación
        token.delete()

        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)