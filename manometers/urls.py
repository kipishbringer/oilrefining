from django.urls import path
from django.views.decorators.cache import cache_page
from manometers.apps import ManometersConfig
from manometers.views import ManometerListView, ManometerCreateView, ManometerUpdateView, \
    ManometerDeleteView, ThermometerCreateView, ThermometerUpdateView, ThermometerDeleteView, PositionListView, \
    PositionCreateView, PositionDeleteView

app_name = ManometersConfig.name

urlpatterns = [
    path('', cache_page(0)(ManometerListView.as_view()), name='manometer-list'),
    path('manometer/create/', cache_page(0)(ManometerCreateView.as_view()), name='manometer-create'),
    path('manometer/update/<int:pk>/', cache_page(0)(ManometerUpdateView.as_view()), name='manometer-update'),
    path('manometer/delete/<int:pk>/', cache_page(0)(ManometerDeleteView.as_view()), name='manometer-delete'),

    path('thermometer/create/', cache_page(0)(ThermometerCreateView.as_view()), name='thermometer-create'),
    path('thermometer/update/<int:pk>/', cache_page(0)(ThermometerUpdateView.as_view()), name='thermometer-update'),
    path('thermometer/delete/<int:pk>/', cache_page(0)(ThermometerDeleteView.as_view()), name='thermometer-delete'),

    path('position/create/', cache_page(0)(PositionCreateView.as_view()), name='position-create'),
    path('position/delete/<int:pk>/', cache_page(0)(PositionDeleteView.as_view()), name='position-delete'),
    path('position/list/', cache_page(0)(PositionListView.as_view()), name='position-list'),

]
