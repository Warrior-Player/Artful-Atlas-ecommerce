# Generated by Django 5.0.3 on 2024-04-08 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_artist_biography_artist_profileartworkimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='style',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='technique',
        ),
        migrations.RemoveField(
            model_name='product',
            name='style',
        ),
        migrations.RemoveField(
            model_name='product',
            name='technique',
        ),
        migrations.AlterField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_images', to='home.product'),
        ),
        migrations.AddField(
            model_name='artist',
            name='style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.style'),
        ),
        migrations.AddField(
            model_name='artist',
            name='technique',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.technique'),
        ),
        migrations.AddField(
            model_name='product',
            name='style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.style'),
        ),
        migrations.AddField(
            model_name='product',
            name='technique',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.technique'),
        ),
    ]
