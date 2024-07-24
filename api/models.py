from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dishes/')
    category = models.ForeignKey(Category, related_name='dishes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    dishes = models.ManyToManyField(Dish, related_name='menus')

    def __str__(self):
        return self.name

class Reservation(models.Model):
    customer = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reservation for {self.customer} on {self.date} at {self.time}"

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    preferences = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
