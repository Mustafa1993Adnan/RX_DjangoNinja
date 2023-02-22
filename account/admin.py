from django.contrib import admin

# Register your models here.
from RX.models import *
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    admin.site.site_header = 'Scientific Office'
    admin.site.site_title = 'Scientific Office'

    list_display = ('email', 'name', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'birth_date', 'gender', 'groups', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_verified')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
