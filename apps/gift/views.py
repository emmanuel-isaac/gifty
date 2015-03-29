from django.shortcuts import render
from django.http import HttpResponse


from rest_framework import viewsets


from apps.gift.serializers import GiftPackSerializer, GiftItemSerializer
from apps.gift.models import GiftPack, GiftItem

# Create your views here.

class GiftItemViewSet(viewsets.ModelViewSet):
    queryset = GiftItem.objects.all()
    serializer_class = GiftItemSerializer


class GiftPackViewSet(viewsets.ModelViewSet):
    queryset = GiftPack.objects.all()
    serializer_class = GiftPackSerializer



def home(request):
	return render(request, 'index.html')

