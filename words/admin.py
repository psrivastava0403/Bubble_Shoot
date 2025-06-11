from django.contrib import admin

# Register your models here.
from .models import AlphabetEntry

@admin.register(AlphabetEntry)
class AlphabetEntryAdmin(admin.ModelAdmin):
    list_display = ('word', 'first_letter')