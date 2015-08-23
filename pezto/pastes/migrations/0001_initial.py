# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('uid', models.CharField(max_length=16, blank=True)),
                ('title', models.CharField(max_length=80, default='Untitled Paste')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('ip_addr', models.GenericIPAddressField()),
            ],
        ),
    ]
