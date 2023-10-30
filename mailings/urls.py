from django.urls import path

from mailings.apps import MailingsConfig

from mailings.views import (display_home, display_clients_menu, ClientListView, ClientCreateView, ClientUpdateView,
                            ClientDeleteView, MailingsListView)

app_name = MailingsConfig.name


urlpatterns = [
    path('', display_home, name='home'),
    path('clients/menu', display_clients_menu, name='client_menu'),
    path('clients/all', ClientListView.as_view(), name='client_list'),
    path('clients/create', ClientCreateView.as_view(), name='client_create'),
    path('clients/update', ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete', ClientDeleteView.as_view(), name='client_delete'),
    path('mailings', MailingsListView.as_view(), name='mailings_list'),
]
