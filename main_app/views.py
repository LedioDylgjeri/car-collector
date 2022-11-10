from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Car, Body
from .forms import MaintenanceForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def cars_index(request):
  cars = Car.objects.filter(user=request.user)
  return render(request, 'cars/index.html', { 'cars': cars })

@login_required
def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  bodies_car_doesnt_have = Body.objects.exclude(
      id__in=car.body.all().values_list('id'))
  maintenance_form = MaintenanceForm()
  return render(request, 'cars/detail.html', { 
    'car': car, 'maintenance_form': maintenance_form, 'bodies': bodies_car_doesnt_have
  })

class CarCreate(LoginRequiredMixin, CreateView):
  model = Car
  fields = ['make', 'model', 'topspeed', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
  model = Car
  fields = ['model', 'topspeed', 'description']

class CarDelete(LoginRequiredMixin, DeleteView):
  model = Car
  success_url = '/cars/'

@login_required
def add_maintenance(request, car_id):
  form = MaintenanceForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.car_id = car_id
    new_maintenance.save()
  return redirect('cars_detail', car_id=car_id)

class BodyCreate(LoginRequiredMixin, CreateView):
  model = Body
  fields = '__all__'

class BodyList(LoginRequiredMixin, ListView):
  model = Body
  fields = ['type', 'color']

class BodyDetail(LoginRequiredMixin, DetailView):
  model = Body
  success_url = '/bodies/'

class BodyUpdate(LoginRequiredMixin, UpdateView):
  model = Body
  fields = ['type', 'color']

class BodyDelete(LoginRequiredMixin, DeleteView):
  model = Body
  success_url = '/bodies/'

@login_required
def assoc_body(request, car_id, body_id):
  Car.objects.get(id=car_id).body.add(body_id)
  return redirect('cars_detail', car_id=car_id)

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
