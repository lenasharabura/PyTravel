from pyexpat import model

from django.contrib import admin

from routes.models import Route

# admin.site.register(Route)


class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_city', 'to_city', 'travel_times')
    list_editable = ['from_city']
    class Meta:
        model = Route

admin.site.register(Route, RouteAdmin)