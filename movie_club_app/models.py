from django.db import models
from django.contrib.auth.models import User
import datetime

User._meta.get_field('email')._unique = True

User._meta.get_field('email')._blank = False
User._meta.get_field('last_name')._blank = False
User._meta.get_field('first_name')._blank = False

class Film(models.Model):
    title = models.CharField(max_length=200, blank=False)
    synopsis = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return "Film: " + self.title

class Cafe(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    address = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return 'Cafe name: {} located at {}'.format(self.name, self.address)

class Meeting(models.Model):
    movie = models.CharField(max_length=200, blank=False, unique=True)
    cafe = models.CharField(max_length=200, blank=False)
    cafeAddress = models.CharField(max_length=200, blank=False)
    time_of_meeting = models.DateTimeField(blank=False)

    def __str__(self):
        return 'On {}, we plan to meet at {}, {}, to discuss the film {}'.format(self.time_of_meeting, self.cafe, self.cafeAddress, self.movie)
