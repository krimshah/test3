# Generated by Django 5.0.2 on 2024-03-24 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_directormaster_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hodmaster',
            name='image',
        ),
    ]
