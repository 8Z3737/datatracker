# Copyright The IETF Trust 2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-06 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0022_reviewer_queue_policy_and_request_assignment_next'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalreviewersettings',
            name='history_change_reason',
            field=models.TextField(null=True),
        ),
    ]