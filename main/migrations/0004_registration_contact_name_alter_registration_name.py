# Generated by Django 4.0.2 on 2023-10-23 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_registration_visa_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='contact_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='name',
            field=models.CharField(max_length=90),
        ),
    ]