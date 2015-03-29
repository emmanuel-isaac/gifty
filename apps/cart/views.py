from django.shortcuts import render
from apps.cart.serializers import CartSerializer
from rest_framework import viewsets
from apps.cart.models import Cart

# Create your views here.
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer