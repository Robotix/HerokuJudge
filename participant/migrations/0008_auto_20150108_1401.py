# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0007_auto_20150108_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='graduation_date',
            new_name='graduation_year',
        ),
    ]
