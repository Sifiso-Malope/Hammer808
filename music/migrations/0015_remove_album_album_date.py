# Generated by Django 3.1.4 on 2021-01-04 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_album_album_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_date',
        ),
    ]