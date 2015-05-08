from rest_framework import serializers

from .models import Order, OrderHistory

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order_historys = serializers.HyperlinkedRelatedField(many=True, view_name='orderhistory-detail', read_only=True)
    class Meta:
        model = Order
        fields = ('order_no','user','order_historys')

class OrderHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderHistory
