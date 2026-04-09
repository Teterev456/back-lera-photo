from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer