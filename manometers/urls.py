from django.urls import path
from django.views.decorators.cache import cache_page
from manometers.apps import ManometersConfig
from manometers.views import ManometerListView, ManometerCreateView, ManometerReadView, ManometerUpdateView, \
    ManometerDeleteView

app_name = ManometersConfig.name

urlpatterns = [
    path('', cache_page(0)(ManometerListView.as_view()), name='manometer-list'),
    path('create/', cache_page(0)(ManometerCreateView.as_view()), name='manometer-create'),
    path('<int:pk>/', cache_page(0)(ManometerReadView.as_view()), name='manometer-read'),
    path('update/<int:pk>/', cache_page(0)(ManometerUpdateView.as_view()), name='manometer-update'),
    path('delete/<int:pk>/', cache_page(0)(ManometerDeleteView.as_view()), name='manometer-delete'),
]