from django.contrib import admin

# Register your models here.
from .models import Ingredient, Dish, BaseDish, Meat, CookingMethod
admin.site.register(Ingredient)
admin.site.register(Dish)
admin.site.register(Meat)
admin.site.register(BaseDish)
admin.site.register(CookingMethod)
