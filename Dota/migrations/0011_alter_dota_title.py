# Generated by Django 3.2.5 on 2021-09-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dota', '0010_auto_20210904_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dota',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Title of tournament'),
        ),
    ]
