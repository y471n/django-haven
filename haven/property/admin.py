from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Property

@admin.register(Property)
class Property(admin.ModelAdmin):
    list_display = ('status', 'value', 'fetched_from', 'propertyId')