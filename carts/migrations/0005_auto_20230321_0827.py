# Generated by Django 3.1 on 2023-03-21 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_cartitem_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='variation',
            new_name='variations',
        ),
    ]