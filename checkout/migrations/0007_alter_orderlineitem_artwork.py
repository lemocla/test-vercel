# Generated by Django 3.2.8 on 2022-01-07 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0015_alter_artwork_stock'),
        ('checkout', '0006_alter_order_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='artwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineartworks', to='artworks.artwork'),
        ),
    ]
