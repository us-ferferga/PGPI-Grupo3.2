from rest_framework.response import Response
from TraineerbookApp.models import Activity, Product
from rest_framework.viewsets import ModelViewSet
from TraineerbookApp.serializer import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
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
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from drf_spectacular.utils import OpenApiParameter
from rest_framework import generics

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

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    @extend_schema(
        description="Obtiene un listado de productos según el ID de la actividad del producto."
    )
    def get_queryset(self):
        activity_id = self.kwargs.get('activity_id')
        return Product.objects.filter(activity__id=activity_id)
      
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
            409: OpenApiResponse(response=None, description="El nombre de usuario ya existe")
        }
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data.get('username')
            
            # Verificar si el nombre de usuario ya existe
            if User.objects.filter(username=username).exists():
                return Response({"error": "El nombre de usuario ya existe"}, status=status.HTTP_409_CONFLICT)

            # Crear el usuario y establecer la contraseña sin guardarlo inmediatamente
            user = serializer.save()

            # Establecer la contraseña y guardar el usuario
            user.set_password(request.data.get('password'))
            user.save()

            # Iniciar sesión automáticamente después del registro
            login(request, user)

            return Response(status=status.HTTP_200_OK)

        # Verificar específicamente si el error es debido al nombre de usuario duplicado
        if 'username' in serializer.errors and 'Ya existe un usuario con este nombre.' in serializer.errors['username']:
            return Response({"error": "El nombre de usuario ya existe"}, status=status.HTTP_409_CONFLICT)

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
   serializer_class = CommentSerializer
   
   @extend_schema(
        request=CommentSerializer,
        description="Pasandole el ID de la actividad, devuelve el listado de comentarios de esa actividad",
        responses={
            201: OpenApiResponse(response=CommentSerializer)}
    )
   def get_queryset(self):
    pk = self.kwargs.get('pk')
    queryset = Comment.objects.all().filter(activity=pk)
    return queryset

class ShoppingCartGetView(APIView):

    @extend_schema(
        description="Obtiene los productos en la cesta del usuario",
        request=None,
        responses={
            200: CartProductSerializer(many=True),
            400: OpenApiResponse(response=None, description="Error en la solicitud")}
    )
    def get(self, request):
        # Recupera y devuelve los productos en la cesta del usuario
        cart_products = request.session.get('cart_products', [])
        serializer = CartProductSerializer(cart_products, many=True)

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
                        'activity_name': product.activity.name,
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
    
class ShoppingCartPutView(APIView):
    serializer_class = CartProductSerializer

    @extend_schema(
        request=None,
        description="Añade o actualiza la cantidad de un producto en la cesta del usuario",
        responses={
            201: CartProductSerializer,
            400: OpenApiResponse(response=None, description="Los datos de la petición son incorrectos")
        }
    )
    def put(self, request, product_id, quantity):
        # Obtén el serializer con los datos de la solicitud
        serializer = self.serializer_class(data={'product_id': product_id, 'quantity': quantity})

        # Verifica la validez del serializer
        if serializer.is_valid():
            # Accede a la cantidad validada
            new_quantity = serializer.validated_data['quantity']
            # Resto del código para manejar el carrito
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            cart_products = request.session.get('cart_products', [])
            updated = False

            for item in cart_products:
                if item['product_id'] == int(product_id):
                    # Actualiza la cantidad del producto en lugar de sumar
                    item['quantity'] = new_quantity
                    updated = True
                    break

            if not updated:
                # Si no se encontró el producto en el bucle, agrégalo al carrito
                cart_products.append({'product_id': int(product_id), 'quantity': new_quantity})

            # Actualiza la sesión con el carrito modificado
            request.session['cart_products'] = cart_products

            # Devuelve una respuesta con los datos del carrito
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        else:
            # Si el serializer no es válido, devuelve los errores
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShoppingCartDeleteView(APIView):
    @extend_schema(
        description="Elimina un producto de la cesta del usuario",
        responses={
            201: OpenApiResponse(response=None),
            404: OpenApiResponse(response=None),
            400: OpenApiResponse(response=None, description="Los datos de la petición son incorrectos")}
    )
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
class CheckoutView(APIView):
    @extend_schema(
        description="Realiza la compra de los productos en el carrito y elimina estos productos del carrito",
        responses={201: ReservationSerializer, 400: OpenApiResponse(response=None, description="Error en la solicitud")}
    )
    def post(self, request):
        # Obtén el usuario actual utilizando CurrentUserView
        user_view = CurrentUserView()
        user_data = user_view.get(request).data

        # Obtén el correo electrónico de la solicitud
        email = request.data.get('user_email', None)

        # Si el usuario no está autenticado, verifica si se proporcionó un correo electrónico
        if not user_data['id']:
            if not email:
                return Response({"detail": "Se requiere la dirección de correo electrónico para completar la compra."},
                                status=status.HTTP_400_BAD_REQUEST)

        # Obtén los productos en el carrito de la sesión
        cart_products = request.session.get('cart_products', [])

        # Verifica que haya productos en el carrito
        if not cart_products:
            return Response({"detail": "El carrito está vacío"}, status=status.HTTP_400_BAD_REQUEST)

        # Crea una reserva para cada producto en el carrito
        reservations = []
        for item in cart_products:
            try:
                product = Product.objects.get(id=item['product_id'])
                quantity = item['quantity']

                # Ajusta la fecha de compra según tus necesidades
                buy_date = product.product_hour_init.date() if product.product_hour_init else None

                # Crea la reserva
                reservation = Reservation.objects.create(
                    user=User.objects.get(pk=user_data['id']),  # Corregido para pasar una instancia de User
                    product=product,
                    buy_date=buy_date,
                    buy_method="online",  # Ajusta el método de compra según tus necesidades
                )

                self.send_confirmation_email(email, reservation, product)

                # Agrega la reserva a la lista de reservas creadas
                reservations.append(reservation)

            except Product.DoesNotExist:
                # Handle the case where the product no longer exists
                pass

        # Elimina los productos del carrito después de la compra
        request.session['cart_products'] = []

        # Serializa y devuelve las reservas creadas
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def send_confirmation_email(self, user, reservation, product):
        # Asunto del correo electrónico
        subject = 'Confirmación de Compra'

        # Si el usuario está autenticado, utiliza su dirección de correo electrónico
        if user and 'id' in user:
            to_email = user['email']
        else:
            # Si el usuario no está autenticado, solicita el correo electrónico manualmente
            to_email = user  # Cambiado a user en lugar de input("Por favor, ingrese su dirección de correo electrónico: ")

        # Cuerpo del correo electrónico en formato HTML
        html_message = render_to_string('email/confirmation_email.html', {'reservation': reservation, 'product': product})

        # Cuerpo del correo electrónico en formato de texto sin formato
        plain_message = strip_tags(html_message)

        # Dirección de correo electrónico desde el cual se enviará el correo
        from_email = 'djangorestpgpi@outlook.com'  # Cambia esto al correo desde el cual enviarás los correos

        # Envía el correo electrónico
        send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)


class GetIncidentApiViewSet(APIView):
    serializer_class = IncidentSerializer

    @extend_schema(
        request=None,
        description="Pasando el ID de una incidencia, devuelve la incidencia por el ID",
        responses={
            200: OpenApiResponse(response=IncidentSerializer)}
    )
    def get(self, request, pk):
        try:
            incident = Incident.objects.get(id=pk)
            serializer = self.serializer_class(incident)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Incident.DoesNotExist:
            return Response({"detail": "Incidencia no encontrada"}, status=status.HTTP_404_NOT_FOUND)

class GetUserIncidentApiViewSet(APIView):
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]
    @extend_schema(
        request=None,
        description="Devuelve las incidencias del usuario autenticado",
        parameters=[OpenApiParameter(name='user_id', location=OpenApiParameter.PATH, description="ID del usuario")],
        responses={
            200: OpenApiResponse(response=IncidentSerializer),
            401: OpenApiResponse(response=None, description="El usuario no está autenticado")}
    )
    def get(self, request):
        user = request.user
        queryset = Incident.objects.filter(user=user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class IncidentCreateApiViewSet(APIView):
    @extend_schema(
        request=IncidentSerializer,
        description="Crea una incidencia. Si el usuario está autenticado, la asocia al usuario.",
        responses={
            201: OpenApiResponse(response=IncidentSerializer),
            400: OpenApiResponse(response=None, description="Los datos de la petición son incorrectos")}
    )
    def post(self, request):
        user = request.user if request.user.is_authenticated else None
        serializer = IncidentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)