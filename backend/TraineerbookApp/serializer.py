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
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

class ShoppingCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField() 
    quantity = serializers.IntegerField(required=False, default=1)

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'



    