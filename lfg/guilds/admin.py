from django.contrib import admin

from lfg.guilds.models import GuildType, Guild, GuildPlaytime


class GuildPlaytimeInline(admin.TabularInline):
    model = GuildPlaytime
    extra = 3


class GuildTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'game')
    search_fields = ['name']
    list_filter = ['game']


class GuildAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'server', 'tagline', 'blurb')
    search_fields = ['name', 'tagline', 'blurb']
    list_filter = ['game', 'server', 'faction', 'guildtype']
    inlines = [GuildPlaytimeInline]

admin.site.register(GuildType, GuildTypeAdmin)
admin.site.register(Guild, GuildAdmin)
