from django.contrib import admin
from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<int:hotel_id>/', views.current_hotel, name='hotel'),
]
