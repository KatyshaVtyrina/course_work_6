from django.contrib import admin

from mailings.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category',)
    search_fields = ('title', 'description',)
    list_filter = ('category',)
