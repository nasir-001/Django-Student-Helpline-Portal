# Generated by Django 3.0 on 2021-04-13 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Helpline_Portal', '0010_auto_20210412_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='courses',
        ),
    ]
