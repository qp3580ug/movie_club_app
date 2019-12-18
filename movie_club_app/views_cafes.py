from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Cafe
from .yelp_api import searchYelp

def cafe_list(request):
    cafes = Cafe.objects.all()
    return render(request, 'movie_club_app/cafes/cafe_list.html', {'cafes': cafes })

def update_cafes(request):
    searchYelp()
    return redirect('movie_club_app:cafe_list')
