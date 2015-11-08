# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pcs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='userID',
        ),
        migrations.AddField(
            model_name='story',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='image',
            field=models.ImageField(null=True, upload_to=b'user-images/', blank=True),
        ),
    ]
