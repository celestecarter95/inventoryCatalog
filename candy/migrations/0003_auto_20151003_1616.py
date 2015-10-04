# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candy', '0002_auto_20150928_1657'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.ForeignKey(related_name='category_group', blank=True, to='candy.Category', null=True),
        ),
    ]
