from django.db import models
from django.contrib.auth.models import UserManager, User as DjangoUser

# Create your models here.

class User(DjangoUser):
    phone = models.PositiveIntegerField(max_length=20, null=True)
    address = models.CharField(max_length=250)
    activation_key = models.CharField(max_length=40, blank=True)
    objects = UserManager()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

User._meta.get_field('first_name').max_length=50
User._meta.get_field('last_name').max_length=50
User._meta.get_field('email').max_length=100
User._meta.get_field('is_staff').default=False
