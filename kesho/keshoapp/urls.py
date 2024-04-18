from django.urls import path
from keshoapp import views

urlpatterns = [
    path('',views.index, name='indexpage'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('babe/', views.AddbabeForm, name='Babe'),
    path('jumper/', views.jumper, name='jumpers'),
    path('base/', views.base, name='base'),


]