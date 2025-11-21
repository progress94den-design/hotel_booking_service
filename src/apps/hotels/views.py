from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from apps.hotels.models import Hotel


def hotels_list(request) -> HttpResponse:
    hotels = Hotel.objects.all()
    data = {
        'title': f'Все отели',
        'hotels':hotels,
    }
    return render(request, 'hotels/hotels_list.html', context=data)


def show_hotel(request, hotel_id) -> HttpResponse:
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    data = {
        'title': f'Отель {hotel.name}',
        'hotel':hotel,
    }
    return render(request, 'hotels/show_hotel.html', context=data)
