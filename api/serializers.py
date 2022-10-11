from rest_framework import serializers
from api.models import Food, MenuFoodItem, Menu, Order, OrderItem


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'price', 'description']


class MenuFoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuFoodItem
        fields = ['id', 'food', 'stock']

    food = FoodSerializer()


class OrderItemOrderSerializer(serializers.ModelSerializer):
    """
    This serializer is for the Order field on every serialized OrderItem
    It will have all the Order fields: client_name, client_email, client_phone,
                                        charge, location, status
    """
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    """
    This serializes the OrderItem that Read, Update, Delete operations will be
    performed on. It had an order field which uses OrderItemOrderSerializer
    """
    class Meta:
        model = OrderItem
        fields = "__all__"

    order = OrderItemOrderSerializer()


class OrderOrderItemSerializer(serializers.ModelSerializer):
    """
    This serializers OrderItems that will be shown when One Order is being queried.
    This is different from OrderItemSerializer because we don't want to show the Order field
    because that would be redundant.

    """
    class Meta:
        model = OrderItem
        exclude = ['order']


class OrderSerializer(serializers.ModelSerializer):
    """
    This serializers the Order that CRUD operations are performed on
    """
    class Meta:
        model = Order
        fields = ['id', 'client_name', 'client_email', 'client_phone', 'charge', 'location', 'status', 'orders']

    orders = OrderOrderItemSerializer(many=True)

