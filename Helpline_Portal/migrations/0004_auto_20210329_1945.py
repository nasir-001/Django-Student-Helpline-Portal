# Generated by Django 3.0 on 2021-03-29 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Helpline_Portal', '0003_auto_20210329_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_teacher',
        ),
    ]
