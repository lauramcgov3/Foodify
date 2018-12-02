# Generated by Django 2.0.6 on 2018-12-02 21:29

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodifyapp', '0002_auto_20181202_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomRecipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('servings', models.IntegerField()),
                ('ingredients', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('method', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('category', models.CharField(max_length=30)),
                ('user', models.TextField(max_length=100)),
                ('originalrecipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='foodifyapp.Recipe')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
    ]