# Generated by Django 4.0.6 on 2022-09-12 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markcheck', '0004_sat_curves'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sat_curves',
            name='curve_type',
        ),
    ]
