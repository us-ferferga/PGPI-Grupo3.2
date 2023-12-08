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
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.decorators import login_required
from drf_yasg.openapi import Response as SwaggerResponse
from drf_yasg.openapi import Schema, TYPE_OBJECT


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

# @swagger_auto_schema(
#     method='post',
#     request_body=UserSerializer,
#     responses={200: 'OK', 400: 'Bad Request'},
# )
# @api_view(['POST'])
# @permission_classes([permissions.AllowAny])
# def register(request):
#     """
#     Endpoint to register a new user.

#     Parameters:
#     - `username` (string): The username of the new user.
#     - `email` (string): The email of the new user.
#     - `password` (string): The password of the new user.

#     Returns:
#     - `id` (int): The ID of the newly registered user.
#     - `username` (string): The username of the newly registered user.
#     - `email` (string): The email of the newly registered user.

#     HTTP Methods:
#     - POST

#     Example:
#     ```
#     curl -X POST -H "Content-Type: application/json" -d '{"username": "newuser", "email": "newuser@example.com", "password": "password123"}' http://your-api-url/register/
#     ```
#     """
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     return Response({'detail': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# @swagger_auto_schema(
#     method='post',
#     request_body=UserLoginSerializer,
#     responses={200: 'OK', 401: 'Unauthorized'},
# )
# @api_view(['POST'])
# @permission_classes([permissions.AllowAny])
# def user_login(request):
#     print(request.user)
#     if request.method == 'POST':
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = authenticate(
#                 username=serializer.validated_data['username'],
#                 password=serializer.validated_data['password']
#             )

#             if user is not None:
#                 login(request, user)

#                 # Crear o recuperar el token de autenticación
#                 token, created = Token.objects.get_or_create(user=user)

#                 return Response({'token': token.key, 'user_id': user.pk }, status=status.HTTP_200_OK)
#             else:
#                 return Response(status=status.HTTP_401_UNAUTHORIZED)

#         return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

#     return Response({'detail': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# @swagger_auto_schema(
#     methods=['get'],
#     responses={200: 'OK'},
# )
# @api_view(['GET'])
# @login_required(login_url=None)
# def logout(request):
#     """
#     Cierre de sesión del usuario.
#     """
#     print('Hola')
#     # request.user.auth_token.delete()


#     # # Revocar el token del usuario
#     # try:
#     #     request.auth.delete()  # Revoca el token
#     # except AttributeError:
#     #     pass  # Si no hay token, simplemente ignóralo

#     return Response({'detail': 'Cierre de sesión exitoso'}, status=status.HTTP_200_OK)

from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.decorators import login_required
from TraineerbookApp.serializer import UserSerializer, UserLoginSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 

class RegisterUserView(APIView):
    permission_classes = [permissions.AllowAny]
    
    @swagger_auto_schema(
        request_body=UserSerializer,  # Especifica el serializador para el cuerpo de la solicitud
        responses={200: 'OK', 400: 'Bad Request'},
    )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    """
    Vista para iniciar sesión de usuarios.
    """
    def post(self, request):
        # Serializar los datos del formulario de inicio de sesión
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            # Intentar autenticar al usuario
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )

            # Verificar si la autenticación fue exitosa
            if user is not None:
                # Iniciar sesión utilizando la función login de Django
                login(request, user)

                # Obtener o crear un token para el usuario
                token, created = Token.objects.get_or_create(user=user)

                # Devolver el token y el ID de usuario en la respuesta
                return Response({'token': token.key, 'user_id': user.pk}, status=status.HTTP_200_OK)
            else:
                # Usuario no autenticado
                return Response({'detail': 'Credenciales no válidas'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Datos del formulario no válidos
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='token',
                in_=openapi.IN_QUERY,
                description='Token de autenticación del usuario',
                type=openapi.TYPE_STRING,
                required=True,
            )
        ]
    )
    def get(self, request):
        # Eliminar el token de autenticación del usuario
        try:
            # Recuperar el token del usuario autenticado y eliminarlo
            token = Token.objects.get(user=request.user)
            token.delete()
        except Token.DoesNotExist:
            pass  # Si el token no existe, simplemente continúa

        return Response({'detail': 'Cierre de sesión exitoso'}, status=status.HTTP_200_OK)