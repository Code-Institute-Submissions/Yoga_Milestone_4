# Generated by Django 3.1.5 on 2021-01-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_lesson_yoga_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='lesson_images/'),
        ),
    ]
