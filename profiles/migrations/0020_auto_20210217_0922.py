# Generated by Django 3.1.5 on 2021-02-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_auto_20210208_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_description',
            field=models.TextField(blank=True, default='', max_length=650),
        ),
    ]
