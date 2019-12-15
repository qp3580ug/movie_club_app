from django.db import models
import requests
from .models import Cafe

def searchYelp(self, zip_code):
        YELP_API_KEY = 'f3n-U3oZBl9eE1_a6_PNLZjs0Phcgs0zQDdaVvuMYq8dBntIB1h5yU9b2-xqBb-FD_i3gPqWY0Mx-BkkITo-V8uQ2LQ5cTXyFAiGn57FuHeSmoMBJFDJ3HwGRumoXXYx'

        yelp_url = 'https://api.yelp.com/v3/businesses/search'

        headers = {'Authorization': 'Bearer ' + YELP_API_KEY}

        params = {
            'categories': 'coffee',
            'location': '55318',
            'radius': '1000',
            'limit': 10,
            'sort_by': 'distance'
        }

        response = requests.get(yelp_url, headers=headers, params=params).json()

        coffee_shops = response['businesses']

        for c in coffee_shops:
            name = c['name']
            location = c['location']
            address = ','.join(location['display_address'])

            Cafe.name.add(name)
            Cafe.address.add(address)