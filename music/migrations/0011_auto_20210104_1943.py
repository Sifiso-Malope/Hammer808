# Generated by Django 3.1.4 on 2021-01-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_photo_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
