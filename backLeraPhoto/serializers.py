from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    chosenDate = serializers.DateField(input_formats=['%d-%m-%Y', '%d/%m/%Y', '%Y-%m-%d'])

    class Meta:
        model = Booking
        fields = '__all__'