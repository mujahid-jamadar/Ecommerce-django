# Generated by Django 3.1 on 2023-03-20 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
        ('carts', '0003_auto_20230319_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]
