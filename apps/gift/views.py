from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic import View


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


class HomeView(View):
	def get(self, request):
		return render_to_response('index.html', locals(), context_instance=RequestContext(request))

