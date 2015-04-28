from django.db import models

# Create your models here.

class GiftItem(models.Model):

    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(max_length=50)
    item_detail = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.name)

    def get_item_giftpacks(self):
        obj = self.giftpacks.all()
        return obj

    class Meta:
        ordering = ('name',)

class GiftPack(models.Model):

    name = models.CharField(max_length=50, blank=False)
    packaging_cost = models.PositiveIntegerField(max_length=15, blank=False)
    gift_items = models.ManyToManyField(GiftItem, blank=False, related_name='giftpacks')

    def __str__(self):
        return '{} {}'.format(self.name, self.packaging_cost)

    def pack_price(self):
        pack_items = self.gift_items.all()
        pack_items_price = 0

        for item in pack_items:
            pack_items_price = pack_items_price + item.price
            continue
        pack_price = self.packaging_cost + pack_items_price

        return pack_price

    def items(self):
        pack_items = ''
        for item in self.gift_items.all():
            pack_items += "{}, ".format(item.name) 
            continue

        return pack_items

    class Meta:
        ordering = ('name',)



