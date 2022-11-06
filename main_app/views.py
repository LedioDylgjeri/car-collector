from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Car:
  def __init__(self, make, model, topspeed, discription):
      self.make = make 
      self.model = model
      self.topspeed = topspeed
      self.discription = discription


cars = [
  Car('Zenovo', 'ST1',  223, 'There are only 15 of these cars.'),
  Car('Ferrari', 'LaFerrari',  217, 'Only 499 cars made from 2013-2016.'),
  Car('Bugatti', 'Veyron',  253, '$1.9 Million if you want one.'),
  Car('Lamborghini', 'Veneno',  221, 'Fastest Lamborghini.')
]


def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  return render(request, 'cars/index.html', { 'cars': cars })