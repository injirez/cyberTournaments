# Generated by Django 3.2.5 on 2021-09-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dota', '0016_alter_gamemode_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitename',
            name='name',
            field=models.CharField(max_length=15, unique=True, verbose_name='Name of the site'),
        ),
    ]