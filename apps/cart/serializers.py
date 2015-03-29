from rest_framework import viewsets, serializers, routers
from apps.cart.models import Cart

class CartSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cart
        fields = ('user', 'cart_number', 'gift_pack', 'order', 'is_paid_for')