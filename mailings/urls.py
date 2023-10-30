from django.urls import path

from mailings.apps import MailingsConfig

from mailings.views import display_home, ClientListView, MailingsListView

app_name = MailingsConfig.name


urlpatterns = [
    path('', display_home, name='home'),
    path('clients', ClientListView.as_view(), name='client_list'),
    path('mailings', MailingsListView.as_view(), name='mailings_list'),
]
