# Generated by Django 2.0.6 on 2019-03-02 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeasemeal_app', '0008_auto_20190302_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familymembers',
            name='familyName',
        ),
        migrations.AddField(
            model_name='familymembers',
            name='famName',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
