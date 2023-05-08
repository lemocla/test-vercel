# Generated by Django 3.2.8 on 2022-01-09 15:30

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_userprofile_wishlist_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='GB', max_length=2, null=True),
        ),
    ]
