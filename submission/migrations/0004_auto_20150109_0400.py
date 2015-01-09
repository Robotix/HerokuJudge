# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_auto_20141225_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='user',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
