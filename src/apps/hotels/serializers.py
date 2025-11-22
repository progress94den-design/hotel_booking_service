from rest_framework import serializers

from apps.hotels.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'price', 'created_at']
        read_only_fields = ['created_at']
