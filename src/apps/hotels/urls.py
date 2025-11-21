from django.contrib import admin
from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    path('', views.hotels_list, name='hotels_list'),
    path('<int:hotel_id>/', views.show_hotel, name='hotel'),
]
