from django.contrib import admin

from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ("match_hometeam_name", "match_awayteam_name")


admin.site.register(Game, GameAdmin)
#@admin.register(Game)
#class PersonAdminModel(UserAdmin):
#    pass

