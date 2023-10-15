from django.urls import path

from mailings.apps import MainConfig

from mailings.views import display_home, ClientListView

app_name = MainConfig.name


urlpatterns = [
    path('', display_home, name='home'),
]
