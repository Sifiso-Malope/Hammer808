# Generated by Django 3.1.4 on 2021-01-03 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20210103_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_date',
            field=models.CharField(max_length=10),
        ),
    ]
