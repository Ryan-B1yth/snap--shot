# Generated by Django 3.2 on 2022-08-03 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
