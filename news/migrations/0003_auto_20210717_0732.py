# Generated by Django 3.2.5 on 2021-07-17 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210717_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
