# Generated by Django 2.2.4 on 2020-03-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_donation', '0003_auto_20200226_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]
