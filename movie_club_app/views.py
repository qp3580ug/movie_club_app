from django.shortcuts import render


def homepage(request):
    return render(request, 'movie_club_app/homepage.html')