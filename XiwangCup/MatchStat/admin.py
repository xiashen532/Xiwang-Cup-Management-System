from django.contrib import admin

# Register your models here.

from .models import Player, Match, Team

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)