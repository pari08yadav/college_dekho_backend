# Generated by Django 5.0.2 on 2024-04-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_college_profile_college_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college_profile',
            name='avtar_url',
        ),
        migrations.AddField(
            model_name='college_profile',
            name='college_image',
            field=models.ImageField(default='Image not found', upload_to='college_images/'),
        ),
    ]