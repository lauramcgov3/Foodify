# Generated by Django 2.0.6 on 2018-12-01 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodifyapp', '0012_auto_20181201_2309'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meal',
            new_name='Recipe',
        ),
    ]
