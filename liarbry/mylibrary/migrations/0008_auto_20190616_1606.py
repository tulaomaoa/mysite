# Generated by Django 2.2.2 on 2019-06-16 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0007_auto_20190616_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylibrary.Publisher'),
        ),
    ]
