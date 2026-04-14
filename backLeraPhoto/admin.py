from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'chosenDate', 'chosenTime', 'chosenType', 'price', 'created_at')
    list_filter = ('chosenType', 'chosenDate', 'created_at')
    search_fields = ('name', 'email', 'chosenType')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)