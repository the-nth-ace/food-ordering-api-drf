from django.contrib import admin
from api.models import Order, OrderItem, Food, Menu, MenuFoodItem

# Register your models here.
admin.register([Order, OrderItem, Food, Menu, MenuFoodItem])