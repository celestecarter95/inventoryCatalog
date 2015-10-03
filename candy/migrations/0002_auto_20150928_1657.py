# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=b'items')),
                ('category', models.ForeignKey(related_name='category_group', to='candy.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='categorygroup',
            name='category',
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(to='candy.Category'),
        ),
        migrations.DeleteModel(
            name='CategoryGroup',
        ),
    ]
