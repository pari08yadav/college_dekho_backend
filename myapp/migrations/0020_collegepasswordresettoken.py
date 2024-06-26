# Generated by Django 5.0.2 on 2024-04-06 12:25

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_alter_college_profile_affiliated_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegePasswordResetToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.faculty')),
            ],
        ),
    ]
