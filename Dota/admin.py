from django.contrib import admin
from .models import Dota, Reward, GameMode, SiteName, Link

admin.site.register(Dota)
admin.site.register(Reward)
admin.site.register(SiteName)
admin.site.register(GameMode)
admin.site.register(Link)
# Register your models here.
