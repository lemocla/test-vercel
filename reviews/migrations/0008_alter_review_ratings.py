# Generated by Django 3.2.8 on 2022-01-04 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_alter_review_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ratings',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5),
        ),
    ]
