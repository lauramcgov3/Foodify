# Generated by Django 2.0.6 on 2019-03-02 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeasemeal_app', '0010_auto_20190302_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymembers',
            name='Admin',
            field=models.BooleanField(),
        ),
    ]
