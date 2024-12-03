from django.contrib import admin

from . models import Termek
# Register your models here.

@admin.register(Termek)
class TermekAdmin(admin.ModelAdmin):
    list_display = ('Nev', 'Kategoria', 'Ar', 'Kiszereles')