from django.contrib import admin
from lfg.user_profile.models import LFGProfile

class LFGProfileAdmin(admin.ModelAdmin):

    class Meta:
        model = LFGProfile

admin.site.register(LFGProfile, LFGProfileAdmin)