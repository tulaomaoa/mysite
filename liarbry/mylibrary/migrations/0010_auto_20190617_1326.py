# Generated by Django 2.2.2 on 2019-06-17 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0009_auto_20190617_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='id',
            new_name='ID',
        ),
    ]
