from django.db import models


class MenuFoodItem(models.Model):
    food = models.ForeignKey('Food', on_delete=models.CASCADE)
    stock = models.IntegerField(default=1)


