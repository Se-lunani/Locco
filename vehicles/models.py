from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vehicles(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveBigIntegerField()
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__ (self):
        return f"{self.make} {self.model} ({self.year})"
    
class Booking(models.Model):
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking {self.id} for {self.vehicle} by {self.user}"



