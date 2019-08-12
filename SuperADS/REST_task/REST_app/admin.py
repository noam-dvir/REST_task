from django.contrib import admin
from .models import logEntry,counter

admin.site.register(logEntry)
admin.site.register(counter)
