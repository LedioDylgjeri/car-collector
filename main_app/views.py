from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Body
from .forms import MaintenanceForm
from django.contrib.auth.views import LoginView

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  bodies_car_doesnt_have = Body.objects.exclude(
      id__in=car.body.all().values_list('id'))
  maintenance_form = MaintenanceForm()
  return render(request, 'cars/detail.html', { 
    'car': car, 'maintenance_form': maintenance_form, 'bodies': bodies_car_doesnt_have
  })

class CarCreate(CreateView):
  model = Car
  fields = ['make', 'model', 'topspeed', 'description']  

class CarUpdate(UpdateView):
  model = Car
  fields = ['model', 'topspeed', 'description']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

def add_maintenance(request, car_id):
  form = MaintenanceForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.car_id = car_id
    new_maintenance.save()
  return redirect('cars_detail', car_id=car_id)

class BodyCreate(CreateView):
  model = Body
  fields = '__all__'

class BodyList(ListView):
  model = Body
  fields = ['type', 'color']

class BodyDetail(DetailView):
  model = Body
  success_url = '/bodies/'

class BodyUpdate(UpdateView):
  model = Body
  fields = ['type', 'color']

class BodyDelete(DeleteView):
  model = Body
  success_url = '/bodies/'

def assoc_body(request, car_id, body_id):
  Car.objects.get(id=car_id).body.add(body_id)
  return redirect('cars_detail', car_id=car_id)

class Home(LoginView):
  template_name = 'home.html'
