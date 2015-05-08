from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    order_no = models.IntegerField()
    user = models.ForeignKey(User)
    note = models.TextField(max_length=200, null=True, blank=True)
    

class OrderHistory(models.Model):
    order = models.ForeignKey(Order, related_name='order_historys')
    price_summary = models.FloatField(default=0.0)
    created_date = models.DateTimeField(auto_now_add=True)
