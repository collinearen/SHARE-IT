# Generated by Django 4.2.6 on 2023-10-22 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_rename_url_user_image_user_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='user_url',
            new_name='website_url',
        ),
    ]