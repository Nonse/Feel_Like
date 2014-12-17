# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20141208_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='reservations.Invoice', null=True),
        ),
    ]
