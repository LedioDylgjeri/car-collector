from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('cars/', views.cars_index, name='cars_index'),
  path('cars/<int:car_id>/', views.cars_detail, name='cars_detail'),
  path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
  path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
  path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
  path('cats/<int:car_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
  path('bodies/create/', views.BodyCreate.as_view(), name='bodies_create'),
  path('bodies/<int:pk>/', views.BodyDetail.as_view(), name='bodies_detail'),
  path('bodies/', views.BodyList.as_view(), name='bodies_index'),
  path('bodies/<int:pk>/update/', views.BodyUpdate.as_view(), name='bodies_update'),
  path('bodies/<int:pk>/delete/', views.BodyDelete.as_view(), name='bodies_delete'),
  path('cars/<int:car_id>/assoc_body/<int:body_id>/', views.assoc_body, name='assoc_body'),
  path('accounts/signup/', views.signup, name='signup'),
]
