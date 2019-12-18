from django.db import models
from .models import Cafe
from django.http import HttpResponse
import requests
from django.shortcuts import redirect


def searchYelp():
    YELP_API_KEY = 'f3n-U3oZBl9eE1_a6_PNLZjs0Phcgs0zQDdaVvuMYq8dBntIB1h5yU9b2-xqBb-FD_i3gPqWY0Mx-BkkITo-V8uQ2LQ5cTXyFAiGn57FuHeSmoMBJFDJ3HwGRumoXXYx'

    yelp_url = 'https://api.yelp.com/v3/businesses/search'

    headers = {'Authorization': 'Bearer ' + YELP_API_KEY}

    params = {
        'categories': 'coffee',
        'location': '55318',
        'radius': '1000',
        'limit': 20,
        'sort_by': 'distance'
    }

    response = requests.get(yelp_url, headers=headers, params=params).json()

    coffee_shops = response['businesses']

    for c in coffee_shops:
        name = c['name']
        location = c['location']
        address = ','.join(location['display_address'])
        
        Cafe.objects.create(name = name, address = address)
        '''cafe = Cafe(name = name, address = address)
        cafe.save()'''
    
    return redirect('movie_club_app:homepage')