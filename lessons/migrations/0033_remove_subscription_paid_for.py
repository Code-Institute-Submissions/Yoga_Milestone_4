# Generated by Django 3.1.5 on 2021-02-08 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0032_auto_20210208_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='paid_for',
        ),
    ]
