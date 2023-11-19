from django.contrib import admin

from mailings.models import Client, MailingsLogs, Mailings


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment',)
    search_fields = ('name', 'email',)
    list_filter = ('name',)


@admin.register(Mailings)
class MailingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_start', 'time_end', 'frequency', 'status')


@admin.register(MailingsLogs)
class MailingsLogsAdmin(admin.ModelAdmin):
    list_display = ('server_response', 'mailing', 'status', 'time')
