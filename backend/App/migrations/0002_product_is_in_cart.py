# Generated by Django 5.0 on 2023-12-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_in_cart',
            field=models.BooleanField(default=False),
        ),
    ]
