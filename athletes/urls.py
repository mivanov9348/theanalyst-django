from django.urls import path
from .views import add_player, all_players, search_players

app_name = "athletes"

urlpatterns = [
    path("add/", add_player, name="add_player"),
    path('search/', search_players, name='search_players'),
    path('all/', all_players, name='all_players'),
]
