# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0008_auto_20150108_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='graduation_year',
            field=models.IntegerField(choices=[(b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019')]),
            preserve_default=True,
        ),
    ]
