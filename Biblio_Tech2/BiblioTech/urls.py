from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.index, name='home'),
  # path('add-student/', views.add_estudante, name='add-student'),
  ]