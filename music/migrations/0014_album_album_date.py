# Generated by Django 3.1.4 on 2021-01-04 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_remove_album_album_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_date',
            field=models.DateField(default='2020-12-12'),
            preserve_default=False,
        ),
    ]
