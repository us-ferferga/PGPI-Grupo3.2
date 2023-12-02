from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


PAY_METHOD = ['online','payback']

class Sala (models.Model):
  name =  models.CharField( null = False, blank=False)

class Profesor (models.Model):
  name =  models.CharField(null = False, blank=False)

class Actividad(models.Model):
  image = models.URLField(max_length=1000, null=True, blank=False)
  description = models.TextField(blank=False)
  teacher = models.ForeignKey(Profesor,on_delete=models.CASCADE, related_name='Profesor')
  class_space = models.ForeignKey(Sala,on_delete=models.CASCADE, related_name='Sala')

class Producto(models.Model):
 product_hour_init = models.DateTimeField(null=True, blank=True)
 product_hour_fin = models.DateTimeField(null=True, blank=True)
 quantity = models.IntegerField(validators=[MinValueValidator(0)])
 price = models.IntegerField(validators=[MinValueValidator(0)])
 actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name='Actividad')

class Reserva(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='User',null=True)
  product = models.ManyToOneRel(Producto, related_name='Producto')
  buy_date = models.DateField(null=True, blank=True)
  buy_method = models.CharField(choices=PAY_METHOD) 

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='User',null=True)
  activity = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name='Actividad')
  content = models.TextField(blank=False)

class Incident(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='User',null=True)
  reservation = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='Reserva')
  content = models.TextField(blank=False)
  

  