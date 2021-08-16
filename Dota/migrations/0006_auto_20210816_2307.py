# Generated by Django 3.2.5 on 2021-08-16 20:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Dota', '0005_alter_dota_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=10, verbose_name='Mode of the game')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(unique=True, verbose_name='URL of tournament')),
                ('tournament', models.URLField(unique=True, verbose_name='URL of tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, verbose_name='Type of reward')),
                ('count', models.CharField(max_length=10, verbose_name='Count of reward')),
                ('currency', models.CharField(max_length=3, verbose_name='Currency of reward')),
            ],
        ),
        migrations.CreateModel(
            name='SiteName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Name of the site')),
            ],
        ),
        migrations.RemoveField(
            model_name='dota',
            name='Tournlink',
        ),
        migrations.RemoveField(
            model_name='dota',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='dota',
            name='img',
        ),
        migrations.AddField(
            model_name='dota',
            name='imgLink',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Dota.link', to_field='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dota',
            name='tournLink',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tournaments', to='Dota.link', to_field='tournament'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dota',
            name='gameMode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dota.gamemode'),
        ),
        migrations.AlterField(
            model_name='dota',
            name='reward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dota.reward'),
        ),
        migrations.AlterField(
            model_name='dota',
            name='siteName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dota.sitename'),
        ),
    ]
