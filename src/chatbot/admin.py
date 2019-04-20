from django.contrib import admin

from .models import UserMessage, BotMessage

admin.site.register(UserMessage)
admin.site.register(BotMessage)
