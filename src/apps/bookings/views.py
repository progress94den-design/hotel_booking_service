from rest_framework import viewsets

from apps.bookings.models import Booking
from apps.bookings.serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
