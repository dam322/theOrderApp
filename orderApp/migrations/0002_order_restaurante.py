# Generated by Django 5.0.4 on 2024-04-06 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderApp', '0001_initial'),
        ('restaurantApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='restaurante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurantApp.restaurant'),
            preserve_default=False,
        ),
    ]