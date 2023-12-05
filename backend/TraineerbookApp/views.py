from django.shortcuts import render
from rest_framework.response import Response
from TraineerbookApp.models import Activity, Product
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, permissions
from TraineerbookApp.serializer import * 
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.inspectors import SerializerInspector
from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

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

@swagger_auto_schema(
    method='post',
    request_body=UserSerializer,
    responses={200: 'OK', 400: 'Bad Request'},
)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    """
    Endpoint to register a new user.

    Parameters:
    - `username` (string): The username of the new user.
    - `email` (string): The email of the new user.
    - `password` (string): The password of the new user.

    Returns:
    - `id` (int): The ID of the newly registered user.
    - `username` (string): The username of the newly registered user.
    - `email` (string): The email of the newly registered user.

    HTTP Methods:
    - POST

    Example:
    ```
    curl -X POST -H "Content-Type: application/json" -d '{"username": "newuser", "email": "newuser@example.com", "password": "password123"}' http://your-api-url/register/
    ```
    """
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Registro exitoso'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'detail': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@swagger_auto_schema(
    method='post',
    request_body=UserLoginSerializer,
    responses={200: 'OK', 401: 'Unauthorized'},
)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )

            if user is not None:
                login(request, user)  # Iniciar sesión tradicional de Django
                return Response({'detail': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    methods=['post'],
    responses={200: 'OK'},
)
@api_view(['POST'])
@csrf_exempt
@login_required(login_url=None) 
def user_logout(request):
    """
    Cierre de sesión del usuario.
    """
    logout(request)  # Cierre de sesión tradicional de Django
    return Response({'detail': 'Cierre de sesión exitoso'}, status=status.HTTP_200_OK)
