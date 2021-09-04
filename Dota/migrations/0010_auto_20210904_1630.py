# Generated by Django 3.2.5 on 2021-09-04 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dota', '0009_alter_dota_starttime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dota',
            name='imgLink',
        ),
        migrations.RemoveField(
            model_name='dota',
            name='tournLink',
        ),
        migrations.AddField(
            model_name='dota',
            name='links',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Dota.link'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='image',
            field=models.URLField(verbose_name='URL of image'),
        ),
        migrations.AlterField(
            model_name='link',
            name='tournament',
            field=models.URLField(verbose_name='URL of tournament'),
        ),
    ]
