from django.urls import path
from measurement.apps import MeasurementConfig

from measurement import views

app_name = MeasurementConfig.name

urlpatterns = [
    # CRUD Subdivision
    path('subdivision/', views.SubdivisionListAPIView.as_view(), name='subdivision-list'),
    path('subdivision/create/', views.SubdivisionCreateAPIView.as_view(), name='subdivision-create'),
    path('subdivision/<int:pk>/', views.SubdivisionRetrieveAPIView.as_view(), name='subdivision-retrieve'),
    path('subdivision/update/<int:pk>/', views.SubdivisionUpdateAPIView.as_view(), name='subdivision-update'),
    path('subdivision/destroy/<int:pk>/', views.SubdivisionDestroyAPIView.as_view(), name='subdivision-destroy'),

    # CRUD Brigade
    path('brigade/', views.BrigadeListAPIView.as_view(), name='brigade-list'),
    path('brigade/create/', views.BrigadeCreateAPIView.as_view(), name='brigade-create'),
    path('brigade/<int:pk>/', views.BrigadeRetrieveAPIView.as_view(), name='brigade-retrieve'),
    path('brigade/update/<int:pk>/', views.BrigadeUpdateAPIView.as_view(), name='brigade-update'),
    path('brigade/destroy/<int:pk>/', views.BrigadeDestroyAPIView.as_view(), name='brigade-destroy'),

    # CRUD Territory
    path('territory/', views.TerritoryListAPIView.as_view(), name='territory-list'),
    path('territory/create/', views.TerritoryCreateAPIView.as_view(), name='territory-create'),
    path('territory/<int:pk>/', views.TerritoryRetrieveAPIView.as_view(), name='territory-retrieve'),
    path('territory/update/<int:pk>/', views.TerritoryUpdateAPIView.as_view(), name='territory-update'),
    path('territory/destroy/<int:pk>/', views.TerritoryDestroyAPIView.as_view(), name='territory-destroy'),

    # CRUD BrigadeTerritoryAssignment
    path('bta/', views.BrigadeTerritoryAssignmentListAPIView.as_view(), name='bta-list'),
    path('bta/create/', views.BrigadeTerritoryAssignmentCreateAPIView.as_view(), name='bta-create'),
    path('bta/<int:pk>/', views.BrigadeTerritoryAssignmentRetrieveAPIView.as_view(), name='bta-retrieve'),
    path('bta/update/<int:pk>/', views.BrigadeTerritoryAssignmentUpdateAPIView.as_view(), name='bta-update'),
    path('bta/destroy/<int:pk>/', views.BrigadeTerritoryAssignmentDestroyAPIView.as_view(), name='bta-destroy'),

    # CRUD Position
    path('position/', views.PositionListAPIView.as_view(), name='position-list'),
    path('position/create/', views.PositionCreateAPIView.as_view(), name='position-create'),
    path('position/<int:pk>/', views.PositionRetrieveAPIView.as_view(), name='position-retrieve'),
    path('position/update/<int:pk>/', views.PositionUpdateAPIView.as_view(), name='position-update'),
    path('position/destroy/<int:pk>/', views.PositionDestroyAPIView.as_view(), name='position-destroy'),

    # CRUD Manometer
    path('manometer/', views.ManometerListAPIView.as_view(), name='manometer-list'),
    path('manometer/create/', views.ManometerCreateAPIView.as_view(), name='manometer-create'),
    path('manometer/<int:pk>/', views.ManometerRetrieveAPIView.as_view(), name='manometer-retrieve'),
    path('manometer/update/<int:pk>/', views.ManometerUpdateAPIView.as_view(), name='manometer-update'),
    path('manometer/destroy/<int:pk>/', views.ManometerDestroyAPIView.as_view(), name='manometer-destroy'),

    # CRUD Thermometer
    path('thermometer/', views.ThermometerListAPIView.as_view(), name='thermometer-list'),
    path('thermometer/create/', views.ThermometerCreateAPIView.as_view(), name='thermometer-create'),
    path('thermometer/<int:pk>/', views.ThermometerRetrieveAPIView.as_view(), name='thermometer-retrieve'),
    path('thermometer/update/<int:pk>/', views.ThermometerUpdateAPIView.as_view(), name='thermometer-update'),
    path('thermometer/destroy/<int:pk>/', views.ThermometerDestroyAPIView.as_view(), name='thermometer-destroy'),
]
