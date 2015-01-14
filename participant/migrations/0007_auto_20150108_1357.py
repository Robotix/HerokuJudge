# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0006_auto_20150108_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='graduation_date',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
