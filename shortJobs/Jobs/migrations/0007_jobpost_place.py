# Generated by Django 3.0.2 on 2020-01-19 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0006_jobpost_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='place',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
