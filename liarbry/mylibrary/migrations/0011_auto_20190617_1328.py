# Generated by Django 2.2.2 on 2019-06-17 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0010_auto_20190617_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='ID',
            new_name='id',
        ),
    ]
