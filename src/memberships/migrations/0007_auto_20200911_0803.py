# Generated by Django 3.0.6 on 2020-09-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0006_auto_20200910_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Profesional', 'pro'), ('Gratis', 'gra'), ('Amateur', 'ama')], default='Gratis', max_length=30),
        ),
    ]
