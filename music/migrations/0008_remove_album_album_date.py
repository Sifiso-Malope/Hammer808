# Generated by Django 3.1.4 on 2021-01-03 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20210103_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_date',
        ),
    ]
