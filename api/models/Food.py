from django.db import models


class Food(models.Model):
    class Food(models.Model):
        name = models.CharField(max_length=255, unique=True)
        price = models.FloatField(default=0)
        description = models.TextField()
        # photo
