from django.db import models

# Create your models here.


class GiftPack(models.Model):

    name = models.CharField(max_length=50, blank=False)
    price = models.PositiveIntegerField(max_length=15, blank=False)

    def __str__(self):
        return '{} {}'.format(self.name, self.price)

class GiftItem(models.Model):

    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(max_length=50)
    item_detail = models.CharField(max_length=250)
    gift_pack = models.ForeignKey(GiftPack)

    def __str__(self):
        return '{}'.format(self.name)


