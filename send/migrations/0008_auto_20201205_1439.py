# Generated by Django 3.1.4 on 2020-12-05 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send', '0007_auto_20201203_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
