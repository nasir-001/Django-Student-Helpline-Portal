# Generated by Django 3.0.5 on 2020-05-23 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Question_Answer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='user',
            new_name='owner',
        ),
    ]