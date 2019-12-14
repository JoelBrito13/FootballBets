from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Person, Token


@admin.register(Person)
class PersonAdminModel(UserAdmin):
    pass


#class TokenAdmin(admin.ModelAdmin):
#    list_display = ('key', 'user', 'created')
#    fields = ('user',)
#    ordering = ('-created',)


admin.site.register(Token)#, TokenAdmin)

