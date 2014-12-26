# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user', models.EmailField(max_length=50)),
                ('source', models.TextField()),
                ('language', models.CharField(max_length=4)),
                ('status', models.TextField()),
                ('queries', models.IntegerField()),
                ('cpu', models.DecimalField(max_digits=5, decimal_places=3)),
                ('memory', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
