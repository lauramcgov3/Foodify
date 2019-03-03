# Generated by Django 2.0.6 on 2019-03-02 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appeasemeal_app', '0017_auto_20190302_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familymembers',
            name='famName',
        ),
        migrations.AddField(
            model_name='familymembers',
            name='familyName',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='familyMembers', to='appeasemeal_app.Family'),
            preserve_default=False,
        ),
    ]
