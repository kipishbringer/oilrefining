# from django import forms
# from measurement.models import Position, Manometer, Thermometer
#
#
# class PositionForm(forms.ModelForm):
#     class Meta:
#         model = Position
#         fields = ('id', 'name', 'group')
#
#
# class ManometerForm(forms.ModelForm):
#     class Meta:
#         model = Manometer
#         fields = ('id', 'position', 'next_verification_date', 'serial_number',
#                   'scale', 'unit', 'notes', 'is_working')
#
#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)
#
#         if self.user:
#             self.fields['position'].queryset = Position.objects.filter(author=self.user)
#
#     def clean(self, *args, **kwargs):
#         cleaned_data = super().clean()
#         position = cleaned_data.get('position')
#         if  position and position.author != self.user:
#             raise forms.ValidationError(f"Вы выбрали позицию другой организации.")
#
# class ThermometerForm(forms.ModelForm):
#     class Meta:
#         model = Thermometer
#         fields = ('id', 'position', 'next_verification_date', 'serial_number',
#                   'scale', 'unit', 'notes', 'is_working')
#
#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)
#
#         if user:
#             self.fields['position'].queryset = Position.objects.filter(author=user)