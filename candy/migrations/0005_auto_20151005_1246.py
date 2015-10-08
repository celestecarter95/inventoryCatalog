# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candy', '0004_auto_20151005_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to=b'pics/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to=b'pics/%Y/%m/%d', blank=True),
        ),
    ]
