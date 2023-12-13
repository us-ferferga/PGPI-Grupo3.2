from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models
from base64 import urlsafe_b64encode

PAY_METHOD = [
    ('online', 'Online Payment'),
    ('payback', 'Payback'),
]

class BlobImage(models.Model):
  content = models.BinaryField()
  mime_type = models.TextField()

  def save_image(self, ruta_archivo):
    from mimetypes import guess_type

    with open(ruta_archivo, 'rb') as f:
      datos = f.read()
    self.content = datos
    self.mime_type = guess_type(ruta_archivo)[0]
    self.save()

  def get_image(self):
    return urlsafe_b64encode(self.content).decode('utf-8')

class ClassRoom(models.Model):
  name =  models.TextField(null = False, blank=False)

class Teacher(models.Model):
  name =  models.TextField(null = False, blank=False)

class Activity(models.Model):
  image = models.ForeignKey(BlobImage, on_delete=models.CASCADE, null=True, blank=False)
  name = models.TextField(blank=False)
  description = models.TextField(blank=False, null = True)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  class_space = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

class Product(models.Model):
 product_hour_init = models.DateTimeField(null=True, blank=True)
 product_hour_fin = models.DateTimeField(null=True, blank=True)
 quantity = models.IntegerField(validators=[MinValueValidator(0)])
 price = models.IntegerField(validators=[MinValueValidator(0)])
 activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

class Reservation(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
  product = models.ForeignKey(Product, on_delete = models.CASCADE, null=True)
  buy_date = models.DateField(null=True, blank=True)
  buy_method = models.TextField(choices=PAY_METHOD) 

class Comment(models.Model):
  user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, null=True)
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
  content = models.TextField(blank=False)

class Incident(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
  reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
  content = models.TextField(blank=False)

class Billing(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
  billing_address = models.TextField(blank=False)

  
