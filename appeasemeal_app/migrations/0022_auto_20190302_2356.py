# Generated by Django 2.0.6 on 2019-03-02 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeasemeal_app', '0021_auto_20190302_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymembers',
            name='Admin',
            field=models.NullBooleanField(),
        ),
    ]
