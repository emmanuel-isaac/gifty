# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftitem',
            name='price',
            field=models.PositiveIntegerField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
