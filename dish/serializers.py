from rest_framework import serializers

from .models import Dish, Ingredient, BaseDish, Meat, CookingMethod


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient


class BaseDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseDish


class MeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meat


class CookingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingMethod