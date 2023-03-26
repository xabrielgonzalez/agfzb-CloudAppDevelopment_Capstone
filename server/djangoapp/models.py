from django.db import models
from django.utils.timezone import now

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # You can add more fields if you want

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dealer_id = models.IntegerField()
    type_choices = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('SPORT', 'Sport'),
    ]
    car_type = models.CharField(max_length=20, choices=type_choices)
    year = models.DateField()
    # You can add more fields if you want

    def __str__(self):
        return self.name


class CarDealer:
    def __init__(self, address, city, state, zipcode, dealer_id, lat, long, name):
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.dealer_id = dealer_id
        self.lat = lat
        self.long = long
        self.name = name


class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date=now()):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
