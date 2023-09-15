# Generated by Django 4.2.5 on 2023-09-10 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_post_image_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
