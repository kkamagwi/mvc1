# Generated by Django 3.2.5 on 2021-07-17 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.tag'),
        ),
    ]