from django.contrib import admin

from mailings.models import Client, MailingsLogs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment',)
    search_fields = ('name', 'email',)
    list_filter = ('name',)


@admin.register(MailingsLogs)
class MailingsLogs(admin.ModelAdmin):
    list_display = ('server_response', 'mailing', 'status', 'time')
