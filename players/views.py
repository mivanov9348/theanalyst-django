from django.shortcuts import render, redirect
from .models import Player

def add_player(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        nationality = request.POST.get("nationality")
        age = request.POST.get("age")
        sport = request.POST.get("sport")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        team = request.POST.get("team") if request.POST.get("team") else None

        Player.objects.create(
            first_name=first_name,
            last_name=last_name,
            nationality=nationality,
            age=age,
            sport=sport,
            height=height,
            weight=weight,
            team=team
        )
        return redirect("core:dashboard")

    return render(request, "players/add_player.html")


def search_players(request):
    pass

def all_players(request):
    pass