from django.http import HttpResponse
from django.shortcuts import render


def bookings_list(request) -> HttpResponse:
    data = {
        'title': 'Бронирование',
        'content': 'Показ всех доступных отелей',
    }
    return render(request, 'bookings/index.html', context=data)


def create_bookings(request, hotel_id) -> HttpResponse:
    data = {
        'title': f'Отель {hotel_id}',
        'content': f'Описание отеля {hotel_id}',
        'hotel_id': hotel_id,
    }
    return render(request, 'bookings/index.html', context=data)
