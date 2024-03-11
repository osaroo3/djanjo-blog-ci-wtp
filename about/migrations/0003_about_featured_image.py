# Generated by Django 4.2.10 on 2024-03-11 04:26

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_collaboraterequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
