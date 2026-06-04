from rest_framework import generics
from measurement.mixins import AuthorQuerySetMixin, CachedListAPIViewMixin, CacheInvalidationMixin
from measurement.permissions import IsOwner
from measurement.models import Position, Manometer, Thermometer, Subdivision, Brigade, Territory, \
    BrigadeTerritoryAssignment
from measurement.serializers import SubdivisionSerializer, BrigadeSerializer, TerritorySerializer, \
    BrigadeTerritoryAssignmentSerializer, PositionSerializer, ManometerSerializer, ThermometerSerializer


"""CRUD Subdivision"""
class SubdivisionListAPIView(CachedListAPIViewMixin, AuthorQuerySetMixin, generics.ListAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()
    cache_namespace = 'subdivision'


class SubdivisionCreateAPIView(CacheInvalidationMixin, generics.CreateAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()
    cache_namespace = 'subdivision'


class SubdivisionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()
    permission_classes = [IsOwner]


class SubdivisionUpdateAPIView(CacheInvalidationMixin, generics.UpdateAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'subdivision'


class SubdivisionDestroyAPIView(CacheInvalidationMixin, generics.DestroyAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'subdivision'


"""CRUD Brigade"""
class BrigadeListAPIView(CachedListAPIViewMixin, AuthorQuerySetMixin, generics.ListAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()
    cache_namespace = 'brigade'


class BrigadeCreateAPIView(CacheInvalidationMixin, generics.CreateAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()
    cache_namespace = 'brigade'


class BrigadeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()
    permission_classes = [IsOwner]


class BrigadeUpdateAPIView(CacheInvalidationMixin, generics.UpdateAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'brigade'


class BrigadeDestroyAPIView(CacheInvalidationMixin, generics.DestroyAPIView):
    serializer_class = BrigadeSerializer
    queryset = Brigade.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'brigade'


"""CRUD Territory"""
class TerritoryListAPIView(CachedListAPIViewMixin, AuthorQuerySetMixin, generics.ListAPIView):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()
    cache_namespace = 'territory'


class TerritoryCreateAPIView(CacheInvalidationMixin, generics.CreateAPIView):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()
    cache_namespace = 'territory'


class TerritoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()
    permission_classes = [IsOwner]


class TerritoryUpdateAPIView(CacheInvalidationMixin, generics.UpdateAPIView):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'territory'


class TerritoryDestroyAPIView(CacheInvalidationMixin, generics.DestroyAPIView):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'territory'


"""CRUD BrigadeTerritoryAssignment"""
class BrigadeTerritoryAssignmentListAPIView(CachedListAPIViewMixin, AuthorQuerySetMixin, generics.ListAPIView):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()
    cache_namespace = 'bta'


class BrigadeTerritoryAssignmentCreateAPIView(CacheInvalidationMixin, generics.CreateAPIView):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()
    cache_namespace = 'bta'


class BrigadeTerritoryAssignmentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()
    permission_classes = [IsOwner]


class BrigadeTerritoryAssignmentUpdateAPIView(CacheInvalidationMixin, generics.UpdateAPIView):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'bta'


class BrigadeTerritoryAssignmentDestroyAPIView(CacheInvalidationMixin, generics.DestroyAPIView):
    serializer_class = BrigadeTerritoryAssignmentSerializer
    queryset = BrigadeTerritoryAssignment.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'bta'


"""CRUD Position"""
class PositionListAPIView(CachedListAPIViewMixin, AuthorQuerySetMixin, generics.ListAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    cache_namespace = 'position'


class PositionCreateAPIView(CacheInvalidationMixin, generics.CreateAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    cache_namespace = 'position'


class PositionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    permission_classes = [IsOwner]


class PositionUpdateAPIView(CacheInvalidationMixin, generics.UpdateAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'position'


class PositionDestroyAPIView(CacheInvalidationMixin, generics.DestroyAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'position'


"""CRUD Manometer"""
class ManometerListAPIView(CachedListAPIViewMixin, AuthorQuerySetMixin, generics.ListAPIView):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()
    cache_namespace = 'manometer'


class ManometerCreateAPIView(CacheInvalidationMixin, generics.CreateAPIView):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()
    cache_namespace = 'manometer'


class ManometerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()
    permission_classes = [IsOwner]


class ManometerUpdateAPIView(CacheInvalidationMixin, generics.UpdateAPIView):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'manometer'


class ManometerDestroyAPIView(CacheInvalidationMixin, generics.DestroyAPIView):
    serializer_class = ManometerSerializer
    queryset = Manometer.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'manometer'


"""CRUD Thermometer"""
class ThermometerListAPIView(CachedListAPIViewMixin, AuthorQuerySetMixin, generics.ListAPIView):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()
    cache_namespace = 'thermometer'


class ThermometerCreateAPIView(CacheInvalidationMixin, generics.CreateAPIView):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()
    cache_namespace = 'thermometer'


class ThermometerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()
    permission_classes = [IsOwner]


class ThermometerUpdateAPIView(CacheInvalidationMixin, generics.UpdateAPIView):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'thermometer'


class ThermometerDestroyAPIView(CacheInvalidationMixin, generics.DestroyAPIView):
    serializer_class = ThermometerSerializer
    queryset = Thermometer.objects.all()
    permission_classes = [IsOwner]
    cache_namespace = 'thermometer'
