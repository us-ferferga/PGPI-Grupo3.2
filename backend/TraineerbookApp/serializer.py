from rest_framework import serializers
from TraineerbookApp.models import *
from rest_framework.serializers import ModelSerializer
from TraineerbookApp.serializer import *


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
    class_space = ClassRoomSerializer()
    
    class Meta:
        model = Activity
        fields = '__all__'




class ProductSerializer(ModelSerializer):
    activity = ActivitySerializer()
    teacher = TeacherSerializer(source='activity.teacher')
    class_space = ClassRoomSerializer(source='activity.class_space')

    class Meta:
        model = Product
        fields = '__all__'

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

