# Generated by Django 2.0.7 on 2020-06-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0003_auto_20200625_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Gratis', 'gra'), ('Profesional', 'pro'), ('Amateur', 'ama')], default='Gratis', max_length=30),
        ),
    ]
