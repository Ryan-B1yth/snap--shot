# Generated by Django 3.2 on 2022-07-05 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default=12345678912, max_length=20),
            preserve_default=False,
        ),
    ]
