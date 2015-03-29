from rest_framework import viewsets, serializers, routers
from apps.order.models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = ('order_number', 'user', 'order_date', 'order_details', 'is_cleared')