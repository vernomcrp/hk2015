from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Dish, Ingredient, BaseDish, Meat, CookingMethod
from .serializers import DishSerializer, IngredientSerializer, BaseDishSerializer, MeatSerializer, CookingMethodSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class BaseDishViewSet(viewsets.ModelViewSet):
    queryset = BaseDish.objects.all()
    serializer_class = BaseDishSerializer


class MeatViewSet(viewsets.ModelViewSet):
    queryset = Meat.objects.all()
    serializer_class = MeatSerializer

class CookingMethodViewSet(viewsets.ModelViewSet):
    queryset = CookingMethod.objects.all()
    serializer_class = CookingMethodSerializer