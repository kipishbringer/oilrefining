from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.core.mail import send_mail
from users.forms import UserRegisterForm
from users.models import User
from config import settings
import secrets

"""Сервис пользователя"""


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('manometers:manometer-list')