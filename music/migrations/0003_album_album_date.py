# Generated by Django 3.1.4 on 2021-01-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20210103_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_date',
            field=models.DateField(default='2020-12-12'),
        ),
    ]
