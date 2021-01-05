# Generated by Django 3.1.5 on 2021-01-05 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_id', models.CharField(editable=False, max_length=32)),
                ('lesson_name', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=254)),
                ('lesson_url', models.URLField(max_length=1024)),
                ('instructor_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='profiles.instructorprofile')),
            ],
        ),
    ]
