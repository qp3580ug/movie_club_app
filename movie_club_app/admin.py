from django.contrib import admin

# Register your models here.
from .models import Film, Theatre, Cafe

admin.site.register(Film)
admin.site.register(Theatre)
admin.site.register(Cafe)