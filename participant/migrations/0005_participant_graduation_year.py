# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0004_auto_20150107_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='graduation_year',
            field=models.DateField(default=django.utils.datetime_safe.date.today),
            preserve_default=False,
        ),
    ]
