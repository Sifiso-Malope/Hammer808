# Generated by Django 3.1.4 on 2021-01-26 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210126_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
