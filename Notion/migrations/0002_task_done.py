# Generated by Django 4.0.6 on 2023-04-20 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
