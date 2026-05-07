from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import ListView
from manometers.forms import PositionForm, ManometerForm, ThermometerForm
from manometers.models import Position, Manometer, Thermometer


"""CRUD Position"""


class PositionCreateView(LoginRequiredMixin, CreateView):

    model = Position
    form_class = PositionForm
    #success_url = reverse_lazy('main:position-list')
    #template_name = 'position_form.html'

    def form_valid(self, position):
        if position.is_valid():
            new_obj = position.save()
            new_obj.author = self.request.user
            new_obj.save()

        return super().form_valid(position)


class PositionReadView(LoginRequiredMixin, DetailView):
    model = Position
    #template_name = 'main/client/client_info.html'


class PositionUpdateView(LoginRequiredMixin, UpdateView):
    model = Position
    form_class = PositionForm


class PositionDeleteView(LoginRequiredMixin, DeleteView):
    model = Position


"""CRUD Manometer"""


class ManometerListView(LoginRequiredMixin, ListView):
    model = Manometer
    template_name = 'manometer_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["manometers"] = Manometer.objects.all()
    #     return context


class ManometerCreateView(LoginRequiredMixin, CreateView):
    model = Manometer
    form_class = ManometerForm

    # success_url = reverse_lazy('main:position-list')
    # template_name = 'position_form.html'

    def form_valid(self, manometer):
        if manometer.is_valid():
            new_obj = manometer.save()
            new_obj.author = self.request.user
            new_obj.save()

        return super().form_valid(manometer)


class ManometerReadView(LoginRequiredMixin, DetailView):
    model = Manometer
    # template_name = 'main/client/client_info.html'


class ManometerUpdateView(LoginRequiredMixin, UpdateView):
    model = Manometer
    form_class = ManometerForm


class ManometerDeleteView(LoginRequiredMixin, DeleteView):
    model = Manometer


"""CRUD Thermometer"""


class ThermometerCreateView(LoginRequiredMixin, CreateView):
    model = Thermometer
    form_class = ThermometerForm

    # success_url = reverse_lazy('main:position-list')
    # template_name = 'position_form.html'

    def form_valid(self, thermometer):
        if thermometer.is_valid():
            new_obj = thermometer.save()
            new_obj.author = self.request.user
            new_obj.save()

        return super().form_valid(thermometer)


class ThermometerReadView(LoginRequiredMixin, DetailView):
    model = Thermometer
    # template_name = 'main/client/client_info.html'


class ThermometerUpdateView(LoginRequiredMixin, UpdateView):
    model = Thermometer
    form_class = ThermometerForm


class ThermometerDeleteView(LoginRequiredMixin, DeleteView):
    model = Thermometer