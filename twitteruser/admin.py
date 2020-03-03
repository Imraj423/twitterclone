from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import TwitterUser


class TwitterUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = TwitterUser


class TwitterUserAdmin(UserAdmin):
    # form = TwitterUserChangeForm

    fieldsets = UserAdmin.fieldsets + ((None, {'fields': (
         'display_name', 'following')}),)


admin.site.register(TwitterUser, TwitterUserAdmin)
