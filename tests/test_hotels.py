import pytest
from apps.hotels.models import Hotel


@pytest.mark.django_db
def test_create_hotel():
    hotel = Hotel.objects.create(name="Test Hotel", price=100)
    assert hotel.name == "Test Hotel"
    assert hotel.price == 100
