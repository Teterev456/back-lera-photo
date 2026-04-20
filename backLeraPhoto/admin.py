from django.contrib import admin
from .models import Booking, BookingCategory

# Register your models here.

@admin.register(BookingCategory)
class BookingCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'type',
        'chosen_date',
        'chosen_time',
        'status',
        'price',
        'created_at'
    )
    list_filter = ('status', 'type', 'all_photo', 'chosen_date', 'created_at')
    search_fields = ('user__username', 'user__email', 'manager_comment')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Клиент и категория', {
            'fields': ('user', 'type')
        }),
        ('Дата и время', {
            'fields': ('chosen_date', 'chosen_time')
        }),
        ('Параметры съёмки', {
            'fields': ('all_photo', 'chosen_count_people', 'chosen_report_hours')
        }),
        ('Статус и стоимость', {
            'fields': ('status', 'price')
        }),
        ('Дополнительная информация', {
            'fields': ('extra_info', 'manager_comment')
        }),
        ('Системное', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )