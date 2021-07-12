# Generated by Django 3.2.5 on 2021-07-12 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dota', '0003_dota_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dota',
            old_name='link',
            new_name='Tournlink',
        ),
        migrations.AddField(
            model_name='dota',
            name='currency',
            field=models.CharField(default=0, max_length=5, verbose_name='Currence of reward'),
            preserve_default=False,
        ),
    ]
