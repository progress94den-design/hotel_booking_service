import pytest
from apps.bookings.serializers import BookingSerializer
from apps.hotels.models import Hotel


@pytest.mark.django_db
def test_create_booking():
    hotel = Hotel.objects.create(name="Test Hotel", price=100.00)
    data = {"hotel": hotel.id, "check_in": "2026-11-23", "check_out": "2026-11-26"}
    serializer = BookingSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    booking = serializer.save()

    assert booking.total_price == 300.00
    assert booking.hotel.name == "Test Hotel"
