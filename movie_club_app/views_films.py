from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Film

def film_details(request, film_pk):
    film = get_object_or_404(Film, pk=film_pk)
    return render(request, 'movie_club_app/Films/film_page.html' , {'film' : film })

def film_list(request):
    films = Film.objects.all()
    return render(request, 'movie_club_app/Films/film_list.html', {'films': films })

def top_films(request):
    films = Film.objects.all()
    return render(request, 'movie_club_app/Films/top_films.html', {'films': films })
