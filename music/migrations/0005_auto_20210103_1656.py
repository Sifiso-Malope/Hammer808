# Generated by Django 3.1.4 on 2021-01-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20210103_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_date',
            field=models.DateField(default=1988),
        ),
    ]
