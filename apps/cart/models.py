from django.db import models
from apps.giftyuser.models import User
from apps.gift.models import GiftPack
from apps.order.models import Order

# Create your models here.

class Cart(models.Model):

    user = models.ForeignKey(User, related_name='carts')
    cart_number = models.PositiveIntegerField(blank=False)
    gift_pack = models.ManyToManyField(GiftPack, related_name='carts')
    order = models.OneToOneField(Order)
    is_paid_for = models.BooleanField(default=False)

    def __str__(self):
        return 'User: {} {}, Cart No: {}'.format(self.user.first_name, self.user.last_name, self.cart_number)
