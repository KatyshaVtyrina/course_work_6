from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailings.forms import ClientForm
from mailings.models import Client, Mailings


def display_home(request):
    return render(request, 'mailings/home.html')


def display_clients_menu(request):
    return render(request, 'mailings/client_menu.html')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:client_list')


class MailingsListView(ListView):
    model = Mailings
    success_url = reverse_lazy('mailings:home')

