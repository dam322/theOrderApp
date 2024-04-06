# Generated by Django 5.0.4 on 2024-04-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0002_remove_product_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
    ]
