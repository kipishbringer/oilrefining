from rest_framework import viewsets, generics
from measurement.models import Position, Manometer, Thermometer, Subdivision, Brigade, Territory, \
    BrigadeTerritoryAssignment
from measurement.serializers import SubdivisionSerializer, BrigadeSerializer, TerritorySerializer, \
    BrigadeTerritoryAssignmentSerializer, PositionSerializer, ManometerSerializer, ThermometerSerializer


"""CRUD Subdivision"""
class SubdivisionListAPIView(generics.ListAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()


class SubdivisionCreateAPIView(generics.ListAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()


class SubdivisionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()


class SubdivisionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()


class SubdivisionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subdivision.objects.all()


"""CRUD Brigade"""
class BrigadeListAPIView(generics.ListAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()


class BrigadeCreateAPIView(generics.ListAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()


class BrigadeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()


class BrigadeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()


class BrigadeDestroyAPIView(generics.DestroyAPIView):
    queryset = Brigade.objects.all()


"""CRUD Territory"""
class TerritoryListAPIView(generics.ListAPIView):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()


class TerritoryCreateAPIView(generics.ListAPIView):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()


class TerritoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()


class TerritoryUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()


class TerritoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Territory.objects.all()


"""CRUD BrigadeTerritoryAssignment"""
class BrigadeTerritoryAssignmentListAPIView(generics.ListAPIView):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()


class BrigadeTerritoryAssignmentCreateAPIView(generics.ListAPIView):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()


class BrigadeTerritoryAssignmentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()


class BrigadeTerritoryAssignmentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()


class BrigadeTerritoryAssignmentDestroyAPIView(generics.DestroyAPIView):
    queryset = BrigadeTerritoryAssignment.objects.all()


"""CRUD Position"""
class PositionListAPIView(generics.ListAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()


class PositionCreateAPIView(generics.ListAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()


class PositionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()


class PositionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()


class PositionDestroyAPIView(generics.DestroyAPIView):
    queryset = Position.objects.all()


"""CRUD Manometer"""
class ManometerListAPIView(generics.ListAPIView):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()


class ManometerCreateAPIView(generics.ListAPIView):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()


class ManometerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()


class ManometerUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()


class ManometerDestroyAPIView(generics.DestroyAPIView):
    queryset = Manometer.objects.all()


"""CRUD Thermometer"""
class ThermometerListAPIView(generics.ListAPIView):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()


class ThermometerCreateAPIView(generics.ListAPIView):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()


class ThermometerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()


class ThermometerUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()


class ThermometerDestroyAPIView(generics.DestroyAPIView):
    queryset = Thermometer.objects.all()