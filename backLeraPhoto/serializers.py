from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Booking, BookingCategory

class BookingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingCategory
        fields = ['id', 'title']

class BookingSerializer(serializers.ModelSerializer):
    chosen_date = serializers.DateField(input_formats=['%d-%m-%Y', '%d/%m/%Y', '%Y-%m-%d'])

    class Meta:
        model = Booking
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user