# Generated by Django 4.1.5 on 2023-02-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='has_toured',
            field=models.BooleanField(default=False),
        ),
    ]
