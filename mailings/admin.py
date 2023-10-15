from django.contrib import admin

from mailings.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment',)
    search_fields = ('name', 'email',)
    list_filter = ('name',)
