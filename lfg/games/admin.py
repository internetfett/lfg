from django.contrib import admin

from lfg.games.models import Game, Faction, CharacterClass, CharacterSubclass, CharacterRole, CharacterRace

class GameAdmin(admin.ModelAdmin):
	list_display = ('name', 'abbr', 'has_factions', 'has_subclasses', 'subclass_class_based', 'subclass_faction_based', 'allows_xfer', 'allows_fc')
	search_fields = ['name']
	
class FactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'game')
    search_fields = ['name']
    list_filter = ['game']
    
class CharacterClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'game')
    search_fields = ['name']
    list_filter = ['game', 'faction']
    
class CharacterSubclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'faction', 'characterclass')
    search_fields = ['name']
    list_filter = ['game', 'faction', 'characterclass']
    
class CharacterRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'game')
    search_fields = ['name']
    list_filter = ['game']
    
class CharacterRaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'game')
    search_fields = ['name']
    list_filter = ['game', 'faction']
	
admin.site.register(Game, GameAdmin)
admin.site.register(Faction, FactionAdmin)
admin.site.register(CharacterClass, CharacterClassAdmin)
admin.site.register(CharacterSubclass, CharacterSubclassAdmin)
admin.site.register(CharacterRole, CharacterRoleAdmin)
admin.site.register(CharacterRace, CharacterRaceAdmin)
