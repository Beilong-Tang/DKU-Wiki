from django.contrib import admin

from .models import Client, Entry, client_entry_updated, Tags
# Register your models here.

admin.site.register(Client)
admin.site.register(Entry)
admin.site.register(client_entry_updated)
admin.site.register(Tags)