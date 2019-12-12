from django.contrib import admin

from .models import Bet, Game

admin.site.register(Bet)
admin.site.register(Game)
#@admin.register(Bet)
#class PersonAdminModel(UserAdmin):
#    pass
