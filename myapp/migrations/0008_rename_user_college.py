# Generated by Django 5.0.2 on 2024-04-02 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_college_profile_subject_teacher'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='College',
        ),
    ]