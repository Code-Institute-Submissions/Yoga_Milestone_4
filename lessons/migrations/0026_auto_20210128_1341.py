# Generated by Django 3.1.5 on 2021-01-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0025_auto_20210128_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='rating',
            field=models.DecimalField(blank=True, choices=[('', 'Choose a rating out of 10'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], decimal_places=0, default='Choose a rating out of 10', max_digits=5, null=True),
        ),
    ]
