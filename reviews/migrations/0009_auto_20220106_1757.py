# Generated by Django 3.2.8 on 2022-01-06 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_alter_order_transaction_id'),
        ('profiles', '0006_userprofile_wishlist_items'),
        ('artworks', '0015_alter_artwork_stock'),
        ('reviews', '0008_alter_review_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='artwork',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='artwork', to='artworks.artwork'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='order_line',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='orderline', to='checkout.orderlineitem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='profiles.userprofile'),
        ),
    ]
