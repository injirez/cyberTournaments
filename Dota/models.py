from django.db import models


class Dota(models.Model):
    title = models.TextField('Title of tournament')
    img = models.TextField('Image of tournament')
    status = models.TextField('Status of tournament')
    startTime = models.TextField('Date of tournament start')
    gameMode = models.TextField('Game mode of tournament')
    participant = models.TextField('Number of participants')
    reward = models.TextField('Tournament reward')
    siteName = models.TextField('Name of site')
    link = models.URLField('URL of tournament', max_length=200)
    dateTime = models.DateTimeField('dateTime')

