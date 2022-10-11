from django.db import models


class SingletonModel(models.Model):
    """
    A singleton is a class that has exactly one instance, and no more.
    For our app, we only need ONE Menu. So this is the correct place to
    use a singleton. This implementation, I copied it off the internet.
    It ensures if a new model is created, it just updates the old model.
    It also ensures the model cannot be deleted.
    It also creates a model if there is none
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


# The Menu Model Inherits from the SingletonModel
class Menu(SingletonModel):
    pass


class MenuFoodItem(models.Model):
    food = models.ForeignKey('Food', on_delete=models.CASCADE)
    stock = models.IntegerField(default=1)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

