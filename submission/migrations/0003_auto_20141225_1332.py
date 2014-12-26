# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0002_submission_problem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='status',
            new_name='stat',
        ),
    ]
