from django.shortcuts import render
from rest_framework.response import Response
from TraineerbookApp.models import Activity, Product
from rest_framework.viewsets import ModelViewSet
from TraineerbookApp.serializer import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from TraineerbookApp.serializer import UserSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated 
from drf_spectacular.utils import extend_schema, OpenApiResponse, inline_serializer
from rest_framework.views import APIView

"""
MUY IMPORTANTE PARA EL FUNCIONAMIENTO DE SWAGGER Y LA CORRECTA COMUNICACIÓN CON EL FRONTEND

Cada vista debe de tener un decorador como el siguiente (este ejemplo es bastante completo pero puede no cubrir todos los casos):
@extend_schema(
        # Este es el serializador de la petición que recibe el servidor
        request=LoginSerializer,
        responses={
            # Aquí describimos la respuesta y los códigos. El inline_serializer es para poder serializar rápidamente objetos muy simples,
            # como es el caso del token de autenticación (así no tenemos que crear un serializador solo para eso)
            # Si por ejemplo estuviéramos mandando una actividad, esto debería de ser un ActivitySerializer
            200: OpenApiResponse(response=inline_serializer(
                    # Cualquiera sirve, simplemente es para identificarlo en la documentación
                    name='TokenResponse',
                    # Poniendo serializers. VSCode debe de sugerirnos todos los tipos de datos si tenemos la extensión de Python instalada (buscar ms-python.python en marketplace)
                    fields={ 'token': serializers.StringRelatedField()}),
                description="Token de autenticación"),
            # None cuando no vamos a enviar nada más aparte del código de estado
            400: OpenApiResponse(response=None, description="Los datos de la petición son incorrectos"),
            401: OpenApiResponse(response=None, description="Las credenciales son incorrectas")}
)

 - Las vistas RegisterUserView, LoginView y LogoutView son ejemplos de buenas implementaciones de controladores para las vistas, **recomendado usarlas de ejemplo** -

Toda la documentación sobre el decorador: https://drf-spectacular.readthedocs.io/en/latest/customization.html

Siempre que se cree un controlador o se haga cualquier cambio en entidades, debe arrancarse el servidor y
accediendo a 127.0.0.1:8080/swagger/ para ver si se ha documentado correctamente.

Para los errores, utilizar exclusivamente códigos HTTP *sin añadir ningún body* que tengan sentido con el problema en cuestión:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
De esta forma en cliente podemos procesar los errores de forma programática y mostrar mensajes de error adecuados en base al estado actual.

Al igual que con el inline_serializer, return Response(status=status...) se debe de autocompletar automáticamente
en VSCode, por lo que no es necesario tener siempre la página de MDN abierta.
"""

"""GET devuelve listado de productos al completo FUNCIONAL"""
class getProductsApiViewSet(ModelViewSet):
    http_method_names = ['get']

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

"""GET devuelve listado de productos segun el id sea igual a la actividad del producto FUNCIONAL"""

class getProductDetailApiViewSet(ModelViewSet):
  serializer_class = ProductSerializer
  
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

    @extend_schema(
        request=UserSerializer,
        responses={
            200: OpenApiResponse(response=None),
            400: OpenApiResponse(response=None, description="Los datos de la petición son incorrectos"),
        }
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
    """
    Inicia la sesión del usuario y devuelve el token de autenticación
    """
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        request=LoginSerializer,
        responses={
            200: OpenApiResponse(response=inline_serializer(
                    name='TokenResponse',
                    fields={ 'token': serializers.StringRelatedField() }),
                description="Token de autenticación"),
            400: OpenApiResponse(response=None, description="Los datos de la petición son incorrectos"),
            401: OpenApiResponse(response=None, description="Las credenciales son incorrectas")}
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

                return Response({'token': token.key }, status=status.HTTP_200_OK)
            else:
                # La contraseña es incorrecta o no existe el usuario
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    """
    Cierra la sesión del usuario eliminando el token de autenticación
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        responses={
            200: OpenApiResponse(response=None),
            304: OpenApiResponse(response=None, description="Django ha detectado un usuario, pero el token no existe, por lo que se considera que la sesión está cerrada"),
            401: OpenApiResponse(response=None, description="El usuario no está autenticado")}
    )
    def post(self, request):
        # Obtener el token asociado al usuario actual
        try:
            token = Token.objects.get(user=request.user)
        except Token.DoesNotExist:
            # Si el token no existe, la sesión ya se considera cerrada
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        # Eliminar el token de autenticación
        token.delete()

        return Response(status=status.HTTP_200_OK)
    

class CurrentUserView(APIView):
    """
    View to get information about the current user.
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=None,
        responses={
            200: OpenApiResponse(response=UserSerializer),
            401: OpenApiResponse(response=None, description="El usuario no está autenticado")}
    )
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateComentView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=CreateCommentSerializer,
        responses={
            201: OpenApiResponse(response=None),
            400: OpenApiResponse(response=None, description="Los datos de la petición son incorrectos"),
            401: OpenApiResponse(response=None, description="El usuario no esta autenticado")}
    )
    def post(self, request):
         # Obtener datos de la solicitud
        data = request.data.copy()

        # Agregar el usuario actual al diccionario de datos
        data['user'] = request.user.id  # Suponiendo que el usuario está autenticado

        # Crear un nuevo serializador con los datos actualizados
        serializer = CreateCommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#GET devuelve 

class GetCommentListApiViewSet(ModelViewSet):
   serializer_class = GetCommentSerializer
   
   @extend_schema(
        request=GetCommentSerializer,
        description="Pasandole el ID de la actividad, devuelve el lsitado de comentarios de esa actividad",
        responses={
            201: OpenApiResponse(response=GetCommentSerializer)}
    )
   def get_queryset(self):
    pk = self.kwargs.get('pk')
    queryset = Comment.objects.all().filter(activity=pk)
    return queryset
        
