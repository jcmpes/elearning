# Generated by Django 3.0.6 on 2020-09-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
