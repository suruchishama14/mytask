from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'class_1', 'section', 'subject')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'class_1', 'section', 'subject', 'password1', 'password2'),
        }),
    )
    list_display = ('first_name', 'last_name', 'email', 'class_1', 'section', 'subject', 'is_active', 'is_staff', 'is_superuser',)
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('first_name',)


admin.site.register(get_user_model(), CustomUserAdmin)