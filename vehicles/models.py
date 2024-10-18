from django.db import models

# Create your models here.
class Vehicles(models.Model):
    MAKE_CHOICES = [
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
        ('Ford', 'Ford'),
        ('BMW', 'BMW'),
        ('Volvo', 'Volvo'),
        ('Mercedes', 'Mercedes'),
    ]
    MODEL_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    ]

    make = models.CharField(max_length=20, choices=MAKE_CHOICES)
    vehicle_name = models.CharField(max_length=50)
    model = models.CharField(max_length=20, choices=MODEL_CHOICES)
    year = models.PositiveSmallIntegerField()
    vin = models.CharField(max_length=17, unique=True, verbose_name="Vehicle Identification Number")
    color = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return  f"{self.vehicle_name} {self.model} {self.vin}"

    class Meta:
        db_table = 'vehicles'