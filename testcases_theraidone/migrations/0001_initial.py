# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testcase',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('bunker_number', models.IntegerField()),
                ('bunker_length', models.CommaSeparatedIntegerField(max_length=100000)),
                ('image', models.ImageField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
