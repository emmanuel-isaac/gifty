# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('cart', '0001_initial'),
        ('giftyuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.OneToOneField(to='order.Order'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(related_name='carts', to='giftyuser.User'),
            preserve_default=True,
        ),
    ]
