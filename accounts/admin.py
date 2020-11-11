# encoding: utf-8
from django.contrib import admin
from accounts.models import FexUser, Invite

# Register your models here.


class FexUserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'is_active',
        'is_admin',
    ]

    list_filter = [
        'is_admin',
    ]

    search_fields = [
        'email',
    ]

class InviteAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_role', 'name', 'contact_phone', 'is_active', )

admin.site.register(FexUser, FexUserAdmin)
admin.site.register(Invite, InviteAdmin)
