# Generated by Django 3.1.4 on 2021-01-04 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20210104_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_date',
            field=models.DateField(default='2020-12-12'),
            preserve_default=False,
        ),
    ]