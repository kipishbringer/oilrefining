from django.contrib import admin
from manometers.models import Manometer, Thermometer, Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'author')
    search_fields = ('id', 'name', 'group', 'author')


@admin.register(Manometer)
class ManometerAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'next_verification_date', 'serial_number', 'scale',
                    'unit', 'notes', 'is_working', 'author')
    search_fields = ('id', 'position', 'next_verification_date', 'serial_number', 'scale',
                    'unit', 'notes', 'is_working', 'author')

@admin.register(Thermometer)
class ThermometerAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'next_verification_date', 'serial_number', 'scale',
                    'unit', 'notes', 'is_working', 'author')
    search_fields = ('id', 'position', 'next_verification_date', 'serial_number', 'scale',
                    'unit', 'notes', 'is_working', 'author')