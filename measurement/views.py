from rest_framework import generics
from measurement.mixins import AuthorQuerySetMixin
from measurement.permissions import IsOwner
from measurement.models import Position, Manometer, Thermometer, Subdivision, Brigade, Territory, \
    BrigadeTerritoryAssignment
from measurement.serializers import SubdivisionSerializer, BrigadeSerializer, TerritorySerializer, \
    BrigadeTerritoryAssignmentSerializer, PositionSerializer, ManometerSerializer, ThermometerSerializer


"""CRUD Subdivision"""
class SubdivisionListAPIView(generics.ListAPIView, AuthorQuerySetMixin):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()


class SubdivisionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()


class SubdivisionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()
    permission_classes = [IsOwner]


class SubdivisionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()
    permission_classes = [IsOwner]


class SubdivisionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()
    permission_classes = [IsOwner]


"""CRUD Brigade"""
class BrigadeListAPIView(generics.ListAPIView, AuthorQuerySetMixin):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()


class BrigadeCreateAPIView(generics.CreateAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()


class BrigadeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()
    permission_classes = [IsOwner]


class BrigadeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()
    permission_classes = [IsOwner]


class BrigadeDestroyAPIView(generics.DestroyAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()
    permission_classes = [IsOwner]


"""CRUD Territory"""
class TerritoryListAPIView(generics.ListAPIView, AuthorQuerySetMixin):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()


class TerritoryCreateAPIView(generics.CreateAPIView):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()


class TerritoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()
    permission_classes = [IsOwner]


class TerritoryUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()
    permission_classes = [IsOwner]


class TerritoryDestroyAPIView(generics.DestroyAPIView):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()
    permission_classes = [IsOwner]


"""CRUD BrigadeTerritoryAssignment"""
class BrigadeTerritoryAssignmentListAPIView(generics.ListAPIView, AuthorQuerySetMixin):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()


class BrigadeTerritoryAssignmentCreateAPIView(generics.CreateAPIView):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()


class BrigadeTerritoryAssignmentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()
    permission_classes = [IsOwner]


class BrigadeTerritoryAssignmentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()
    permission_classes = [IsOwner]


class BrigadeTerritoryAssignmentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()
    permission_classes = [IsOwner]


"""CRUD Position"""
class PositionListAPIView(generics.ListAPIView, AuthorQuerySetMixin):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()


class PositionCreateAPIView(generics.CreateAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()


class PositionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    permission_classes = [IsOwner]


class PositionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    permission_classes = [IsOwner]


class PositionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    permission_classes = [IsOwner]


"""CRUD Manometer"""
class ManometerListAPIView(generics.ListAPIView, AuthorQuerySetMixin):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()


class ManometerCreateAPIView(generics.CreateAPIView):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()


class ManometerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()
    permission_classes = [IsOwner]


class ManometerUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()
    permission_classes = [IsOwner]


class ManometerDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()
    permission_classes = [IsOwner]


"""CRUD Thermometer"""
class ThermometerListAPIView(generics.ListAPIView, AuthorQuerySetMixin):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()


class ThermometerCreateAPIView(generics.CreateAPIView):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()


class ThermometerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()
    permission_classes = [IsOwner]


class ThermometerUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()
    permission_classes = [IsOwner]


class ThermometerDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()
    permission_classes = [IsOwner]