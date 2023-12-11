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

class CartProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required = True)
    quantity = serializers.IntegerField(required = True)

class GetProductSerializer(serializers.Serializer):
    activity_description = serializers.CharField(source='activity.description', required=False)
    product_hour_init = serializers.DateTimeField()
    product_hour_fin = serializers.DateTimeField()
    quantity = serializers.IntegerField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)






    