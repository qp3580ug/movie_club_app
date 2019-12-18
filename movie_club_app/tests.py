import unittest
from django.test import TestCase
from .models import Film, Meeting
from .forms import AddFilmForm, NewMeetingForm, UpdateCafes
from django.db import IntegrityError
from django.urls import reverse

class TestForms(TestCase):

    def test_rating_is_only_one_length(self):
        add_film_data = {'rating' : '55'}
        form = AddFilmForm(add_film_data)
        self.assertFalse(form.is_valid())

    def test_cafe_missing_from_data(self):
        meeting_data = {'movie': 'test movie', 'cafeAddress': '321 test Ave', 'time_of_meeting': '12/23/20'}
        form = NewMeetingForm(meeting_data)
        self.assertFalse(form.is_valid())

    def test_update_cafe_data_added_is_valid(self):
        cafe_data = {'name': 'test cafe', 'address': '321 test Ave'}
        form = UpdateCafes(cafe_data)
        self.assertTrue(form.is_valid())

class TestModels(TestCase):

    def test_duplicate_films_fails(self):

        film = Film(title='Terminator', synopsis='Test Synopsis', rating='5')
        film.save()

        film2 = Film(title='Terminator', synopsis='Test Synopsis 2', rating='3')
        with self.assertRaises(IntegrityError):
            film2.save()

class TestViews(TestCase):
    def test_results_for_film_search(self):
            response = self.client.get( reverse('movie_club_app:film_list') , {'search_name' : 'Psycho'} )
            self.assertNotContains(response, 'Terminator')
            self.assertNotContains(response, 'The Grinch')
            self.assertNotContains(response, 'Scott Pilgrim vs. The World')
            self.assertEqual(len(response.context['films']), 0)
            self.assertTemplateUsed(response, 'movie_club_app/Films/film_list.html')