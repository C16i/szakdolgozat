# Generated by Django 4.2.16 on 2024-12-13 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fooldal', '0002_cart_cartitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='products',
            new_name='product',
        ),
    ]