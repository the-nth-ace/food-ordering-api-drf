from api.models import Food, MenuFoodItem
from api.serializers import FoodSerializer, MenuFoodItemSerializer
from rest_framework import generics


# Create your views here.
class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class MenuFoodItemList(generics.ListCreateAPIView):
    queryset = MenuFoodItem.objects.all()
    serializer_class = MenuFoodItemSerializer


class MenuFoodItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer



