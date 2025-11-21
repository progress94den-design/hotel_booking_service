from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    data = {
        'title': 'Главная',
        'content': 'Отели',
    }
    return render(request,'hotels/index.html', context=data)


def about(request) -> HttpResponse:
    data = {
        'title': 'О сайте',
        'content': 'Бла бла бла, о нас и еще немного о нас',
    }
    return render(request,'hotels/index.html', context=data)


def current_hotel(request, hotel_id) -> HttpResponse:
    data = {
        'title': f'Отель {hotel_id}',
        'content': f'Описание отеля {hotel_id}',
        'hotel_id': hotel_id,
    }
    return render(request,'hotels/index.html', context=data)