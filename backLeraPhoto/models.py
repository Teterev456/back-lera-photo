from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    chosenType = models.CharField(max_length=50)
    chosenDate = models.DateField()
    chosenTime = models.CharField(max_length=5)
    allPhoto = models.BooleanField(default=False)
    chosenCountPeople = models.PositiveIntegerField()
    chosenReportHours = models.PositiveIntegerField()
    extraInfo = models.TextField(blank=True)
    price = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.chosenDate} {self.chosenTime}"