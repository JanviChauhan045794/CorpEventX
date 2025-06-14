# Generated by Django 5.1.7 on 2025-04-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_banner_event_registration_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('employee', 'Employee'), ('student', 'Student'), ('industry', 'Industry Professional'), ('academia', 'Academic'), ('admin', 'Admin')], default='employee', max_length=20),
        ),
    ]
