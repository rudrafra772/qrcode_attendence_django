# Generated by Django 4.1.7 on 2023-03-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendenc',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
