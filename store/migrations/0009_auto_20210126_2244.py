# Generated by Django 3.1.4 on 2021-01-26 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210126_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
    ]