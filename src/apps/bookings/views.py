from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from apps.bookings.models import Booking


def bookings_list(request) -> HttpResponse:
    bookings = Booking.objects.all()
    data = {
        'title': 'Забронированые отели',
        'bookings': bookings,
    }
    return render(request, 'bookings/bookings_list.html', context=data)


def create_bookings(request, booking_id) -> HttpResponse:
    booking = get_object_or_404(Booking, pk=booking_id)
    data = {
        'title': f'Инфа о броне {booking.id}',
        'content': booking
    }
    return render(request, 'bookings/index.html', context=data)
