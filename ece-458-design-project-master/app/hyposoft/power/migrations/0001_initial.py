# Generated by Django 3.0.4 on 2020-03-30 09:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('changeplan', '0001_initial'),
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networked', models.BooleanField()),
                ('position', models.CharField(choices=[('L', 'Left'), ('R', 'Right')], max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Powered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plug_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Asset must be plugged into a plug from 1 to 24 on this PDU.'), django.core.validators.MaxValueValidator(24, message='Asset must be plugged into a plug from 1 to 24 on this PDU.')])),
                ('on', models.BooleanField(default=False)),
                ('order', models.IntegerField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Asset')),
                ('pdu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='power.PDU')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='changeplan.ChangePlan')),
            ],
            options={
                'unique_together': {('order', 'asset', 'version'), ('plug_number', 'pdu', 'version')},
            },
        ),
        migrations.AddField(
            model_name='pdu',
            name='assets',
            field=models.ManyToManyField(through='power.Powered', to='equipment.Asset'),
        ),
        migrations.AddField(
            model_name='pdu',
            name='rack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Rack'),
        ),
        migrations.AddField(
            model_name='pdu',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='changeplan.ChangePlan'),
        ),
        migrations.AlterUniqueTogether(
            name='pdu',
            unique_together={('rack', 'position', 'version')},
        ),
    ]
