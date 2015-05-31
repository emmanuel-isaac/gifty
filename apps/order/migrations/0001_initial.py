# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giftyuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_number', models.PositiveIntegerField()),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('order_details', models.CharField(max_length=250)),
                ('is_cleared', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to='giftyuser.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
