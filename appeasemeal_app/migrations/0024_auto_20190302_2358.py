# Generated by Django 2.0.6 on 2019-03-02 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeasemeal_app', '0023_auto_20190302_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymembers',
            name='Admin',
            field=models.IntegerField(default=1),
        ),
    ]
