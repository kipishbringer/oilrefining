from main import views
from main.apps import MainConfig
from django.urls import path

app_name = MainConfig.name

urlpatterns = [
    path('api/weather/', views.WeatherAPIView.as_view(), name='weather'),
    path('api/markets/', views.MarketsAPIView.as_view(), name='markets'),
]
