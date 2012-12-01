from django.contrib import admin
from lfg.user_messages.models import UserMessage

class UserMessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserMessage, UserMessageAdmin)