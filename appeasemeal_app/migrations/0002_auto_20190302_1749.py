# Generated by Django 2.0.6 on 2019-03-02 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeasemeal_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='family',
            options={},
        ),
        migrations.AddField(
            model_name='family',
            name='ID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='family',
            unique_together={('ID', 'familyName')},
        ),
    ]
