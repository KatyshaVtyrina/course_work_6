from django.shortcuts import render

from django.views.generic import ListView

from mailings.models import Client, Mailings


def display_home(request):
    return render(request, 'mailings/home.html')


class ClientListView(ListView):
    model = Client


class MailingsListView(ListView):
    model = Mailings

