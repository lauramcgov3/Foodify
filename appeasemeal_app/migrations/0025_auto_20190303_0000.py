# Generated by Django 2.0.6 on 2019-03-03 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeasemeal_app', '0024_auto_20190302_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymembers',
            name='Admin',
            field=models.BooleanField(default=1),
        ),
    ]
