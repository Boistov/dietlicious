from django import forms
from .models import Category, Dish, Menu, Reservation, Customer

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'image', 'category']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'dishes']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer', 'date', 'time', 'num_guests', 'special_requests']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['user', 'phone_number', 'address', 'preferences']
