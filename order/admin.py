from django.contrib import admin

# Register your models here.
from .models import Order, OrderHistory

admin.site.register(Order)
admin.site.register(OrderHistory)
