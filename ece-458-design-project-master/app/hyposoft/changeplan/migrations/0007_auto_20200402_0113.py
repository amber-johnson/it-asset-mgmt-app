# Generated by Django 3.0.3 on 2020-04-02 01:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changeplan', '0006_auto_20200402_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetdiff',
            name='message',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=512), size=None),
        ),
    ]
