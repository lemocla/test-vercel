# Generated by Django 3.2.8 on 2021-12-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'verbose_name': 'Mailing List'},
        ),
        migrations.AlterField(
            model_name='mailing',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
