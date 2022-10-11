from django.contrib import admin
from api.models import Order, OrderItem, Food,  MenuFoodItem

# Register your models here.
admin.site.register([Order, OrderItem, Food,  MenuFoodItem])

