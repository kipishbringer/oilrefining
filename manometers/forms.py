from django import forms
from manometers.models import Position, Manometer, Thermometer


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ('id', 'name', 'group')


class ManometerForm(forms.ModelForm):
    class Meta:
        model = Manometer
        fields = ('id', 'position', 'next_verification_date', 'serial_number',
                  'scale', 'unit', 'notes', 'is_working')


class ThermometerForm(forms.ModelForm):
    class Meta:
        model = Thermometer
        fields = ('id', 'position', 'next_verification_date', 'serial_number',
                  'scale', 'unit', 'notes', 'is_working')