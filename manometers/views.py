from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from manometers.forms import PositionForm, ManometerForm, ThermometerForm
from manometers.models import Position, Manometer, Thermometer


class OwnerMixin(UserPassesTestMixin):

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

"""CRUD Position"""


class PositionCreateView(LoginRequiredMixin, CreateView):

    model = Position
    form_class = PositionForm

    success_url = '/manometers/position/list/'
    #success_url = reverse_lazy('main:position-list')
    #template_name = 'position_form.html'

    def form_valid(self, position):
        if position.is_valid():
            new_obj = position.save()
            new_obj.author = self.request.user
            new_obj.save()

        return super().form_valid(position)


class PositionListView(LoginRequiredMixin, ListView):

    model = Position
    template_name = 'position_list.html'

    login_url = '/users/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["positions"] = Position.objects.filter(author=self.request.user)
        return context


class PositionDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):

    model = Position

    success_url = '/manometers/position/list/'


"""CRUD Manometer"""


class ManometerListView(LoginRequiredMixin, ListView):

    model = Manometer
    template_name = 'manometer_list.html'

    login_url = '/users/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["manometers"] = Manometer.objects.filter(author=self.request.user)
        context["thermometers"] = Thermometer.objects.filter(author=self.request.user)
        return context


class ManometerCreateView(LoginRequiredMixin, CreateView):

    model = Manometer
    form_class = ManometerForm
    success_url = '/manometers/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, manometer):
        if manometer.is_valid():
            new_obj = manometer.save()
            new_obj.author = self.request.user
            new_obj.save()

        return super().form_valid(manometer)


class ManometerUpdateView(LoginRequiredMixin, OwnerMixin, UpdateView):

    model = Manometer
    form_class = ManometerForm

    success_url = '/manometers/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ManometerDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):

    model = Manometer

    success_url = '/manometers/'


"""CRUD Thermometer"""


class ThermometerCreateView(LoginRequiredMixin, CreateView):

    model = Thermometer
    form_class = ThermometerForm
    success_url = '/manometers/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


    def form_valid(self, thermometer):
        if thermometer.is_valid():
            new_obj = thermometer.save()
            new_obj.author = self.request.user
            new_obj.save()

        return super().form_valid(thermometer)


class ThermometerUpdateView(LoginRequiredMixin, OwnerMixin, UpdateView):

    model = Thermometer
    form_class = ThermometerForm
    success_url = '/manometers/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ThermometerDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):

    model = Thermometer
    success_url = '/manometers/'