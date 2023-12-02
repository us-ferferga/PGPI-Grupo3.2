from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


PAY_METHOD = ['online','payback']

class ClassRoom (models.Model):
  name =  models.CharField( null = False, blank=False)

class Teacher (models.Model):
  name =  models.CharField(null = False, blank=False)

class Activity(models.Model):
  image = models.URLField(max_length=1000, null=True, blank=False)
  description = models.TextField(blank=False)
  teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE, related_name='Teacher')
  class_space = models.ForeignKey(ClassRoom,on_delete=models.CASCADE, related_name='ClassRoom')

class Product(models.Model):
 product_hour_init = models.DateTimeField(null=True, blank=True)
 product_hour_fin = models.DateTimeField(null=True, blank=True)
 quantity = models.IntegerField(validators=[MinValueValidator(0)])
 price = models.IntegerField(validators=[MinValueValidator(0)])
 activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='Activity')

class Reservation(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='User',null=True)
  product = models.ManyToOneRel(Product, related_name='Product')
  buy_date = models.DateField(null=True, blank=True)
  buy_method = models.CharField(choices=PAY_METHOD) 

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='User',null=True)
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='Activity')
  content = models.TextField(blank=False)

class Incident(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='User',null=True)
  reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='Reservation')
  content = models.TextField(blank=False)
  

  