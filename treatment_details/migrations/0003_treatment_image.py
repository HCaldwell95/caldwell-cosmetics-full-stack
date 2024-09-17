# Generated by Django 4.2.15 on 2024-09-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment_details', '0002_remove_treatment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='image',
            field=models.ImageField(default='static/images/illumi-treatment-card.jpg', upload_to='treatments/'),
            preserve_default=False,
        ),
    ]
