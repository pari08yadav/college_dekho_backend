# Generated by Django 5.0.2 on 2024-04-07 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_alter_college_password_alter_faculty_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
