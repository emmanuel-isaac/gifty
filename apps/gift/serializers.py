from rest_framework import viewsets, serializers, routers
from apps.gift.models import GiftPack, GiftItem

class GiftItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GiftItem
        fields = ('url', 'name')

class GiftPackSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GiftPack
        fields = ('url', 'item', 'name', 'price')
