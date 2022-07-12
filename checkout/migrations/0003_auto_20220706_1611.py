# Generated by Django 3.2 on 2022-07-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_basket',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]