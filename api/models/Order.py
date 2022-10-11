from django.utils.translation import gettext_lazy as _
from django.db import models


class OrderItem(models.Model):
    MenuFoodItem = models.ForeignKey('Food', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        SETTLED = 'STL', _('Settled')
        FAILED = "FAIL",  _('Failed')
        PENDING = "PEN", _('Pending')

    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=12)
    charge = models.FloatField(default=0)
    location = models.TextField()
    status = models.CharField(max_length=7, choices=OrderStatus.choices, default=OrderStatus.PENDING)
