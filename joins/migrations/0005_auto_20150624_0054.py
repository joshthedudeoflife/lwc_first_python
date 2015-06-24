# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0004_auto_20150622_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
