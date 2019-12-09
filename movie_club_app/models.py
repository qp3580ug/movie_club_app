from django.db import models
from django.contrib.auth.models import User
import datetime

User._meta.get_field('email')._unique = True

User._meta.get_field('email')._blank = False
User._meta.get_field('last_name')._blank = False
User._meta.get_field('first_name')._blank = False

class Film(models.Model):
    title = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return "Film: " + self.title

class Theatre(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    address = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=2, blank=False)

    def __str__(self):
        return 'Theatre name: {} located at {} {}, {}'.format(self.name, self.address, self.city, self.state)

class Cafe(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    address = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=2, blank=False)

    def __str__(self):
        return 'Cafe name: {} located at {} {}, {}'.format(self.name, self.address, self.city, self.state)

