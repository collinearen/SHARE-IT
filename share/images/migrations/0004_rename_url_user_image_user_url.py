# Generated by Django 4.2.6 on 2023-10-22 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_image_url_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='url_user',
            new_name='user_url',
        ),
    ]