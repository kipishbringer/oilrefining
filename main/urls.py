from main import views
from main.apps import MainConfig
from django.urls import path
from django.views.decorators.cache import cache_page
from django.contrib.auth.views import LoginView, LogoutView

app_name = MainConfig.name

urlpatterns = []
