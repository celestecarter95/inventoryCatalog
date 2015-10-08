# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candy', '0003_auto_20151003_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=b'pics/%Y/%m/%d, blank=True, null=True'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to=b'pics/%Y/%m/%d, blank=True, null=True'),
        ),
    ]
