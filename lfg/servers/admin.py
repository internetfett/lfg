from django.contrib import admin

from lfg.servers.models import ServerRegion, ServerType, ServerTimezone, Server

class ServerRegionAdmin(admin.ModelAdmin):
	list_display = ('name', 'game')
	search_fields = ['name']
	list_filter = ['game']

class ServerTypeAdmin(admin.ModelAdmin):
	list_display = ('name', 'game')
	search_fields = ['name']
	list_filter = ['game']
	
class ServerTimezoneAdmin(admin.ModelAdmin):
	list_display = ('name', 'game')
	search_fields = ['name']
	list_filter = ['game']
	
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'region', 'type', 'timezone')
    search_fields = ['name']
    list_filter = ['game', 'region', 'type', 'timezone']    

admin.site.register(ServerRegion, ServerRegionAdmin)
admin.site.register(ServerType, ServerTypeAdmin)
admin.site.register(ServerTimezone, ServerTimezoneAdmin)
admin.site.register(Server, ServerAdmin)
