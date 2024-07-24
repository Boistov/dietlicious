from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(Reservation)


