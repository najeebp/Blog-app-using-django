# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog3', '0002_post_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
    ]
