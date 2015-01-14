# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0003_auto_20150107_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='state',
            field=models.CharField(max_length=5, choices=[(b'IN-AP', b'Andhra Pradesh'), (b'IN-AR', b'Arunachal Pradesh'), (b'IN-AS', b'Assam'), (b'IN-BR', b'Bihar'), (b'IN-CT', b'Chhattisgarh'), (b'IN-GA', b'Goa'), (b'IN-GJ', b'Gujarat'), (b'IN-HR', b'Haryana'), (b'IN-HP', b'Himachal Pradesh'), (b'IN-JK', b'Jammu and Kashmir'), (b'IN-JH', b'Jharkhand'), (b'IN-KA', b'Karnataka'), (b'IN-KL', b'Kerala'), (b'IN-MP', b'Madhya Pradesh'), (b'IN-MH', b'Maharashtra'), (b'IN-MN', b'Manipur'), (b'IN-ML', b'Meghalaya'), (b'IN-MZ', b'Mizoram'), (b'IN-NL', b'Nagaland'), (b'IN-OR', b'Odisha'), (b'IN-PB', b'Punjab'), (b'IN-RJ', b'Rajasthan'), (b'IN-SK', b'Sikkim'), (b'IN-TN', b'Tamil Nadu'), (b'IN-TG', b'Telangana'), (b'IN-TR', b'Tripura'), (b'IN-UT', b'Uttarakhand'), (b'IN-UP', b'Uttar Pradesh'), (b'IN-WB', b'West Bengal'), (b'IN-AN', b'Andaman and Nicobar Islands'), (b'IN-CH', b'Chandigarh'), (b'IN-DN', b'Dadra and Nagar Haveli'), (b'IN-DD', b'Daman and Diu'), (b'IN-DL', b'Delhi'), (b'IN-LD', b'Lakshadweep'), (b'IN-PY', b'Puducherry')]),
            preserve_default=True,
        ),
    ]
