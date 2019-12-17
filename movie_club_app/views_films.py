from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Film
from .forms import AddFilmForm

def film_details(request, film_pk):
    film = get_object_or_404(Film, pk=film_pk)
    return render(request, 'movie_club_app/Films/film_page.html' , {'film' : film })

def film_list(request):
    films = Film.objects.all()
    return render(request, 'movie_club_app/Films/film_list.html', {'films': films })

@login_required
def add_film(request):
    if request.method == 'POST':
        form = AddFilmForm(request.POST, request.FILES, instance=None)
        if form.is_valid():
            film = form.save(commit=False)
            film.save()
            return redirect('movie_club_app:film_list', film_pk=film.pk)
    
    else :
        form = AddFilmForm()

    return render(request, 'movie_club_app/Films/add_film.html' , { 'form' : form })