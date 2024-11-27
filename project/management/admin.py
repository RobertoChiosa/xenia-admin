from django.contrib import admin

from .models import Host, Property

admin.site.register(Host)
admin.site.register(Property)