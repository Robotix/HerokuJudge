# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0002_auto_20150107_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='mobileNo',
            field=models.DecimalField(max_digits=13, decimal_places=0),
            preserve_default=True,
        ),
    ]
