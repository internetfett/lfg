from django.contrib import admin

from lfg.players.models import Player, PlayerPlaytime

class PlayerPlaytimeInline(admin.TabularInline):
    model = PlayerPlaytime
    extra = 3
    
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'server', 'level', 'blurb')
    search_fields = ['name', 'blurb']
    list_filter = ['game', 'server', 'faction']
    inlines = [PlayerPlaytimeInline]
	
admin.site.register(Player, PlayerAdmin)
