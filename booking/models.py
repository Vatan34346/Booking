from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    table_number = models.PositiveIntegerField()
    guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Table: {self.table_number} on {self.date} {self.time} is booked for {self.guests} people"


