# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paste',
            name='password',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
