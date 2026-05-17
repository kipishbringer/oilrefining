from rest_framework import serializers
from measurement.models import Subdivision, Brigade, Territory, BrigadeTerritoryAssignment, Position, Manometer, \
    Thermometer


class SubdivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields = '__all__'


class BrigadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brigade
        fields = '__all__'


class TerritorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Territory
        fields = '__all__'


class BrigadeTerritoryAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrigadeTerritoryAssignment
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class ManometerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manometer
        fields = '__all__'


class ThermometerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thermometer
        fields = '__all__'