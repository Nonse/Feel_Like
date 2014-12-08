# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20141012_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'verbose_name_plural': 'Coaches'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Company'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='reservation',
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(blank=True, to='reservations.Customer', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='invoice',
            field=models.ForeignKey(blank=True, to='reservations.Invoice', null=True),
            preserve_default=True,
        ),
    ]
