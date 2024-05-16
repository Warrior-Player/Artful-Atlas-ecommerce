# Generated by Django 5.0.3 on 2024-05-11 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_rename_full_name_profile_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='stripe_payment_intent',
        ),
        migrations.AddField(
            model_name='cartorderitems',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.product'),
        ),
    ]