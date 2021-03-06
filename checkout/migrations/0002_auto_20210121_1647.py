# Generated by Django 3.1.5 on 2021-01-21 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_auto_20210115_1125'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile'),
            preserve_default=False,
        ),
    ]
