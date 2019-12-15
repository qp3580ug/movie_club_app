from django.contrib import admin

# Register your models here.
from .models import Film, Cafe, Meeting

admin.site.register(Film)
admin.site.register(Cafe)
admin.site.register(Meeting)