# Generated by Django 5.0.3 on 2024-04-11 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_philosophy_subjectmatter_alter_artistreview_artist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='style',
            name='image',
        ),
        migrations.RemoveField(
            model_name='technique',
            name='image',
        ),
    ]
