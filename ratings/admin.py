from django.contrib import admin
from .models import Rating, Location
# Register your models here.

class RatingAdmin(admin.ModelAdmin):
    list_display = ['location', 'date_created', 'like', 'dislike']
    list_filter = ['location']

admin.site.register(Rating, RatingAdmin)

class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ('location_link',)

admin.site.register(Location, LocationAdmin)

