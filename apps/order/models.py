from django.db import models
from apps.giftyuser.models import User

# Create your models here.

class Order(models.Model):

    order_number = models.PositiveIntegerField(blank=False)
    user = models.ForeignKey(User)
    order_date = models.DateTimeField(auto_now=True)
    order_details = models.CharField(max_length=250)
    is_cleared = models.BooleanField(default=False)

    def __str__(self):
        return 'Order No: {}'.format(self.order_number)