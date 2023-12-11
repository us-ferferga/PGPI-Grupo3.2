from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

PAY_METHOD = [
    ('online', 'Online Payment'),
    ('payback', 'Payback'),
]
 
class ClassRoom (models.Model):
  name =  models.CharField(max_length=100, null = False, blank=False)

class Teacher (models.Model):
  name =  models.CharField(max_length=100, null = False, blank=False)

class Activity(models.Model):
  image = models.URLField(max_length=1000, null=True, blank=False)
  description = models.TextField(blank=False)
  teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE, related_name='activities')
  class_space = models.ForeignKey(ClassRoom,on_delete=models.CASCADE, related_name='activities')

class Product(models.Model):
 product_hour_init = models.DateTimeField(null=True, blank=True)
 product_hour_fin = models.DateTimeField(null=True, blank=True)
 quantity = models.IntegerField(validators=[MinValueValidator(0)])
 price = models.IntegerField(validators=[MinValueValidator(0)])
 activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='products')

class Reservation(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='reservations',null=True)
  product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='reservations', null=True)
  buy_date = models.DateTimeField(null=True, blank=True)
  buy_method = models.CharField(max_length=10, choices=PAY_METHOD) 

class Comment(models.Model):
  user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name='comments',null=True)
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='comments')
  content = models.TextField(blank=False)

class Incident(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='incidents',null=True)
  reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='incidents')
  content = models.TextField(blank=False)
  
