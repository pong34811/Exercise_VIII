# views.py
from django.shortcuts import render, redirect
from .models import Anime_list

def index(request):
    animes = Anime_list.objects.all()
    return render(request, 'index.html', {"animes": animes})

def delete(request, anime_id):
    anime = Anime_list.objects.get(id=anime_id)
    anime.delete()
    return redirect('/')  
