# Generated by Django 5.0.3 on 2024-03-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='donde',
            field=models.BooleanField(default=False),
        ),
    ]
