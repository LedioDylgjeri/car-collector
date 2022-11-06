from django.db import models

# Create your models here.
class Car(models.Model):
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  topspeed = models.IntegerField()
  description = models.TextField(max_length=200)

  def __str__(self):
    return self.make