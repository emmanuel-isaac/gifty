from django.db import models
from django.contrib.auth.models import UserManager, User as DjangoUser

# Create your models here.

class User(DjangoUser):
    phone = models.PositiveIntegerField(blank=False, max_length=20,)
    address = models.CharField(max_length=250)

    objects = UserManager()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

User._meta.get_field('first_name').max_length=50
User._meta.get_field('last_name').max_length=50
User._meta.get_field('email').max_length=100


class StaffMember(models.Model):

    user = models.OneToOneField(User)

    def __unicode__(self):
        return '{}'.format(self.user.username)

    def save(self, *args, **kwargs):
       user = User.objects.get(pk = self.user.pk)
       user.is_staff = True
       user.save()
       super(StaffMember, self).save(*args, **kwargs)
