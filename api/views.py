from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Dish, Menu, Reservation, Customer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_form.html'
    fields = ['name']
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category_form.html'
    fields = ['name']
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category-list')


class DishListView(ListView):
    model = Dish
    template_name = 'dish_list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            return Dish.objects.filter(category_id=category_id)
        return Dish.objects.all()

class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish_detail.html'
    context_object_name = 'dish'

class DishCreateView(CreateView):
    model = Dish
    template_name = 'dish_form.html'
    fields = ['name', 'description', 'price', 'image', 'category']
    success_url = reverse_lazy('dish-list')

class DishUpdateView(UpdateView):
    model = Dish
    template_name = 'dish_form.html'
    fields = ['name', 'description', 'price', 'image', 'category']
    success_url = reverse_lazy('dish-list')

class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'dish_confirm_delete.html'
    success_url = reverse_lazy('dish-list')


class MenuListView(ListView):
    model = Menu
    template_name = 'menu_list.html'
    context_object_name = 'menus'

class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu_detail.html'
    context_object_name = 'menu'

class MenuCreateView(CreateView):
    model = Menu
    template_name = 'menu_form.html'
    fields = ['name', 'description', 'dishes']
    success_url = reverse_lazy('menu-list')

class MenuUpdateView(UpdateView):
    model = Menu
    template_name = 'menu_form.html'
    fields = ['name', 'description', 'dishes']
    success_url = reverse_lazy('menu-list')

class MenuDeleteView(DeleteView):
    model = Menu
    template_name = 'menu_confirm_delete.html'
    success_url = reverse_lazy('menu-list')


class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'reservation_list.html'
    context_object_name = 'reservations'

class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = 'reservation_detail.html'
    context_object_name = 'reservation'

class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    template_name = 'reservation_form.html'
    fields = ['customer', 'date', 'time', 'num_guests', 'special_requests']
    success_url = reverse_lazy('reservation-list')

class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    template_name = 'reservation_form.html'
    fields = ['customer', 'date', 'time', 'num_guests', 'special_requests']
    success_url = reverse_lazy('reservation-list')

class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservation
    template_name = 'reservation_confirm_delete.html'
    success_url = reverse_lazy('reservation-list')


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['user', 'phone_number', 'address', 'preferences']
    success_url = reverse_lazy('customer-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['user', 'phone_number', 'address', 'preferences']
    success_url = reverse_lazy('customer-list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer-list')


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})
