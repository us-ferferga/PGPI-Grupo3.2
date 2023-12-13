from rest_framework import serializers
from TraineerbookApp.models import *
from rest_framework.serializers import ModelSerializer
from TraineerbookApp.serializer import *
from base64 import b64encode
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

class BlobImageSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = BlobImage
        fields = ('data',)

    @extend_schema_field(OpenApiTypes.STR)
    def get_data(self, obj):
        return 'data:' + obj.mime_type + ';charset=utf-8;base64,' + b64encode(obj.content).decode('utf-8')

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class ClassRoomSerializer(ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'

class ActivitySerializer(ModelSerializer):
    teacher = TeacherSerializer()
    image = BlobImageSerializer()
    class_space = ClassRoomSerializer()
    
    class Meta:
        model = Activity
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    teacher = TeacherSerializer()
    class_space = ClassRoomSerializer()

    class Meta:
        model = Product
        fields = '__all__'

class CartProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required = True)
    quantity = serializers.IntegerField(required = True)

class GetProductSerializer(serializers.Serializer):
    activity_name = serializers.CharField(source='activity.name', required=False)
    product_hour_init = serializers.DateTimeField()
    product_hour_fin = serializers.DateTimeField()
    quantity = serializers.IntegerField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    Fields:
    - `id` (int): The ID of the user.
    - `username` (string): The username of the user.
    - `email` (string): The email of the user.
    - `password` (string): The password of the user.

    Note:
    - The `password` field is write-only, and it should be sent during user registration.
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.

    Fields:
    - `username` (string): The username of the user.
    - `password` (string): The password of the user.
    """

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)



class CommentSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content']

class CreateCommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'user', 'activity', 'content']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

