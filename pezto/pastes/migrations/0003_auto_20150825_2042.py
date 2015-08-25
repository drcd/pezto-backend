# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastes', '0002_paste_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paste',
            options={'ordering': ('created_at',)},
        ),
    ]
