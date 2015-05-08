from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Order, OrderHistory
from .serializers import OrderSerializer, OrderHistorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderHistoryViewSet(viewsets.ModelViewSet):
    queryset = OrderHistory.objects.all()
    serializer_class = OrderHistorySerializer
