# Generated by Django 3.0.3 on 2020-04-02 00:08

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('changeplan', '0005_auto_20200402_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetdiff',
            name='conflicts',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='networkportdiff',
            name='conflicts',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
