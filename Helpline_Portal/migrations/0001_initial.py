# Generated by Django 3.0.4 on 2020-03-23 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('regnumber', models.CharField(max_length=10)),
                ('level', models.CharField(max_length=1)),
            ],
        ),
    ]
