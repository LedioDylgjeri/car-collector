from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

SERVICES = (
  ('W', 'Car Wash'),
  ('O', 'Oil Change'),
  ('T', 'Tire Change')
)

class Body(models.Model):
  type = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.type

  def get_absolute_url(self):
    return reverse('bodies_detail', kwargs={'pk': self.id})

class Car(models.Model):
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  topspeed = models.IntegerField()
  description = models.TextField(max_length=200)
  body = models.ManyToManyField(Body)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.make

  def get_absolute_url(self):
    return reverse('cars_detail', kwargs={'car_id': self.id})

  def serviced_today(self):
    return self.maintenance_set.filter(date=date.today()).count() >= len(SERVICES)

class Maintenance(models.Model):
  date = models.DateField('Service Date')
  service = models.CharField(
    max_length=1,
    choices=SERVICES,  
    default=SERVICES[0][0]
  )

  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_service_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

