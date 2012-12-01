from django.contrib import admin
from lfg.user_profile.models import LFGProfile

class LFGProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(LFGProfile, LFGProfileAdmin)