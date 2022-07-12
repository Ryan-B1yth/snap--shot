# Generated by Django 3.2 on 2022-07-11 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('default_county', models.CharField(blank=True, max_length=50, null=True)),
                ('default_city', models.CharField(blank=True, max_length=50, null=True)),
                ('default_address_1', models.CharField(blank=True, max_length=50, null=True)),
                ('default_address_2', models.CharField(blank=True, max_length=50, null=True)),
                ('default_postcode', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]