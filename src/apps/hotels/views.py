from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets, mixins, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from apps.hotels.models import Hotel
from apps.hotels.serializers import HotelSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']
