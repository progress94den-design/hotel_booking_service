from datetime import date

from django.db.models import Q
from rest_framework import serializers

from apps.bookings.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id', 'hotel',
            'check_in', 'check_out', 'total_price', 'created_at'
        ]
        read_only_fields = ['created_at']

    def validate(self, data):
        check_in = data.get('check_in')
        check_out = data.get('check_out')
        hotel = data.get('hotel')

        # Проверка что дата выезда после даты заезда
        if check_in >= check_out:
            raise serializers.ValidationError("Дата выезда должна быть позже даты заезда")

        # Проверка что дата заезда не в прошлом
        if check_in < date.today():
            raise serializers.ValidationError("Дата заезда не может быть в прошлом")

        # Проверка брони отеля на эти даты
        overlapping_bookings = Booking.objects.filter(hotel=hotel)

        overlapping_bookings = overlapping_bookings.filter(
            Q(check_in__lt=check_out) | Q(check_out__gt=check_in)
        )

        if overlapping_bookings.exists():
            raise serializers.ValidationError("Отель уже забронирован на указанные даты")

        return data

    def create(self, validated_data):
        hotel = validated_data['hotel']
        check_in = validated_data['check_in']
        check_out = validated_data['check_out']
        nights = (check_out - check_in).days
        total_price = hotel.price * nights

        validated_data['total_price'] = total_price

        return super().create(validated_data)