# Generated by Django 4.2.5 on 2023-09-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image_fondo',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]