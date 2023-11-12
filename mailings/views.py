import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from blog.models import Post
from mailings.forms import ClientForm, MailingForm, MessageForm
from mailings.models import Client, Message
from mailings.tasks import *


class HomeView(TemplateView):

    template_name = 'mailings/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        mailings = Mailings.objects
        context_data['mailing_all'] = mailings.all().count()
        context_data['mailing_active'] = mailings.filter(status='CREATED').count()
        context_data['unique_clients'] = Client.objects.distinct().count()
        context_data['posts_list'] = random.sample(list(Post.objects.all()), 3)
        return context_data


@login_required
def display_clients_menu(request):
    return render(request, 'mailings/client_menu.html')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:client_list')


@login_required
def display_mailings_menu(request):
    return render(request, 'mailings/mailings_menu.html')


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailings


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailings


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailings
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form):
        if form.is_valid():
            # создание рассылки
            mailings = Mailings.objects.create(
                time_start=form.cleaned_data['time_start'],
                time_end=form.cleaned_data['time_end'],
                frequency=form.cleaned_data['frequency'],
                message=form.cleaned_data['message'],
                user=self.request.user
            )
            # создание клиентов
            mailings.clients.set(form.cleaned_data['clients'])

            # парсим дату
            date_start = parser.parse(str(form.cleaned_data['time_start']))

            # если время старта в будущем, отправляем рассылку по времени старта
            if date_start > timezone.now():
                create_mailing.s(
                    form.cleaned_data['time_start'],
                    form.cleaned_data['time_end'],
                    mailings.id,
                    form.cleaned_data['message'].subject,
                    form.cleaned_data['message'].body,
                ).apply_async(eta=date_start)
            # в ином случае отправляем сразу
            else:
                create_mailing.s(
                    form.cleaned_data['time_start'],
                    form.cleaned_data['time_end'],
                    mailings.id,
                    form.cleaned_data['message'].subject,
                    form.cleaned_data['message'].body,
                ).apply_async()

            mailings.status = 'STARTED'
            mailings.save()
        return redirect('mailings:mailing_menu')


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailings
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailings
    success_url = reverse_lazy('mailings:mailing_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:mailing_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailings:mailing_list')

