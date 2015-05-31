from django.db import models
from django.contrib.auth.models import UserManager, User as DjangoUser

# Create your models here.

class User(DjangoUser):
    phone = models.PositiveIntegerField(max_length=20, null=True)
    address = models.CharField(max_length=250)
    activation_key = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
