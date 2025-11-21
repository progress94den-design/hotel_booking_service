from django.urls import path

from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.bookings_list, name='bookings_list'),
    path('<int:hotel_id>/', views.create_bookings, name='create_booking'),
]
