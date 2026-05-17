from users.apps import UsersConfig
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = UsersConfig.name

urlpatterns = []
