from rest_framework import serializers
from TraineerbookApp.models import *
from rest_framework.serializers import ModelSerializer
from TraineerbookApp.serializer import *

class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class ClassRoomSerializer(ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'

class GetProductSerializer(ModelSerializer):
    activity = ActivitySerializer()
    teacher = TeacherSerializer(source='activity.teacher')
    class_space = ClassRoomSerializer(source='activity.class_space')

    class Meta:
        model = Product
        fields = '__all__'

class GetProductSerializer2(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
