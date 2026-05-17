from django.contrib import admin
from measurement.models import Manometer, Thermometer, Position, Subdivision, Brigade, Territory, \
    BrigadeTerritoryAssignment


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subdivision', 'territory', 'device_type', 'author')
    search_fields = ('id', 'name', 'subdivision', 'territory', 'device_type', 'author')


@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author')
    search_fields = ('id', 'name', 'author')


@admin.register(Brigade)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subdivision', 'author')
    search_fields = ('id', 'name', 'subdivision', 'author')


@admin.register(Territory)
class TerritoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'territory_type', 'subdivision', 'author')
    search_fields = ('id', 'name', 'territory_type', 'subdivision', 'author')


@admin.register(BrigadeTerritoryAssignment)
class BrigadeTerritoryAssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'brigade', 'territory', 'author')
    search_fields = ('id', 'brigade', 'territory', 'author')


@admin.register(Manometer)
class ManometerAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'next_verification_date', 'serial_number', 'scale',
                    'unit', 'notes', 'is_working', 'subdivision', 'author')
    search_fields = ('id', 'position', 'next_verification_date', 'serial_number', 'scale',
                    'unit', 'notes', 'is_working', 'subdivision', 'author')

@admin.register(Thermometer)
class ThermometerAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'next_verification_date', 'serial_number', 'scale',
                    'unit', 'notes', 'is_working', 'subdivision', 'author')
    search_fields = ('id', 'position', 'next_verification_date', 'serial_number', 'scale',
                    'unit', 'notes', 'is_working', 'subdivision', 'author')