# Generated by Django 3.0 on 2021-04-12 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Helpline_Portal', '0009_auto_20210412_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='course',
            new_name='courses',
        ),
    ]