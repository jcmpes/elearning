# Generated by Django 3.0.6 on 2020-09-10 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0005_auto_20200910_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Gratis', 'gra'), ('Profesional', 'pro'), ('Amateur', 'ama')], default='Gratis', max_length=30),
        ),
    ]
