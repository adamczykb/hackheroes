from django.contrib import admin
from mapa.models import Point
# Register your models here.
@admin.register(Point)
class PersonAdmin(admin.ModelAdmin):
    pass
