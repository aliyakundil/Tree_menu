# Generated by Django 4.1.7 on 2023-03-31 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_parent_menu_parent_menu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='explicit_url',
            new_name='url_menu',
        ),
    ]