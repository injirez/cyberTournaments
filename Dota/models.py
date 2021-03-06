from django.db import models


class Dota(models.Model):
    title = models.CharField('Title of tournament', max_length=100, unique=True)
    status = models.CharField('Status of tournament', max_length=15)
    startTime = models.CharField('Date of tournament start', max_length=25)
    gameMode = models.ForeignKey('GameMode', on_delete=models.CASCADE, related_name='gameModes')
    participant = models.CharField('Number of participants', max_length=10)
    reward = models.ForeignKey('Reward', on_delete=models.CASCADE)
    siteName = models.ForeignKey('SiteName', on_delete=models.CASCADE, related_name='siteNames')
    links = models.ForeignKey('Link', on_delete=models.CASCADE)
    ip = models.CharField('IP address', max_length=15)

class Reward(models.Model):
    type = models.CharField('Type of reward', max_length=15)
    count = models.CharField('Count of reward', max_length=10)
    currency = models.CharField('Currency of reward', max_length=3)

class GameMode(models.Model):
    mode = models.CharField('Mode of the game', max_length=10, unique=True)

class SiteName(models.Model):
    name = models.CharField('Name of the site', max_length=15, unique=True)

class Link(models.Model):
    image = models.URLField('URL of image', max_length=200)
    tournament = models.URLField('URL of tournament', max_length=200)

