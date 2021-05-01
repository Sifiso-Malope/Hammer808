# Generated by Django 3.1.4 on 2021-01-26 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_product_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='author',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
    ]
