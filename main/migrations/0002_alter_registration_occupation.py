# Generated by Django 4.0.2 on 2023-10-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='occupation',
            field=models.CharField(max_length=10),
        ),
    ]
