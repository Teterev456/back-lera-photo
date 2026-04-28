from django.db import models
from django.conf import settings
# Create your models here.

class BookingCategory(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('confirmed', 'Подтверждён'),
        ('completed', 'Завершён'),
        ('cancelled', 'Отменён'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings',
        null=True,
        blank=True
    )
    type = models.ForeignKey(
        BookingCategory,
        on_delete=models.PROTECT,
        related_name='bookings',
        null=True,
        blank=True
    )
    chosen_date = models.DateField()
    chosen_time = models.CharField(max_length=5)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    all_photo = models.BooleanField(default=False)
    chosen_count_people = models.PositiveIntegerField(blank=True, null=True)
    chosen_report_hours = models.PositiveIntegerField(blank=True, null=True)
    extra_info = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    manager_comment = models.TextField(blank=True)

    def __str__(self):
        return f"Booking #{self.id} by {self.user.username}"

class BookingChat(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    booking = models.ForeignKey(
        'Booking',
        on_delete=models.CASCADE,
        related_name='messages'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Message {self.id} for Booking {self.booking.id}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"