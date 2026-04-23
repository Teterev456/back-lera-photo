from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Booking, BookingCategory, BookingChat

class BookingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingCategory
        fields = ['id', 'title']

class BookingSerializer(serializers.ModelSerializer):
    chosen_date = serializers.DateField(input_formats=['%d-%m-%Y', '%d/%m/%Y', '%Y-%m-%d'])

    class Meta:
        model = Booking
        fields = '__all__'

class BookingChatSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')
    is_admin = serializers.SerializerMethodField()

    class Meta:
        model = BookingChat
        fields = ['id', 'author_id', 'author_name', 'text', 'created_at', 'is_admin']
        read_only_fields = ['id', 'created_at', 'author', 'booking']

    def get_is_admin(self, obj):
        return obj.author.is_staff

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