# Generated by Django 4.2.15 on 2024-09-17 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treatment_details', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='image',
        ),
    ]
