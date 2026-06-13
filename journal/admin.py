from django.contrib import admin
from .models import JournalEntry


@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'mood', 'created_at')
    list_filter = ('mood', 'created_at')
    search_fields = ('title', 'content')
