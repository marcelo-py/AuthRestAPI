from django.contrib import admin
from .models import UserAuth


class UserAuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_display_links = ('username', )


admin.site.register(UserAuth, UserAuthAdmin)