# Generated by Django 3.1.5 on 2021-01-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0008_auto_20210107_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]