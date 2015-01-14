# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0005_participant_graduation_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='graduation_year',
            new_name='graduation_date',
        ),
    ]
