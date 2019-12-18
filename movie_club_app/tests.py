from django.test import TestCase
from .models import Film, Meeting
from .forms import AddFilmForm, NewMeetingForm, UpdateCafes
from django.db import IntegrityError
from . import views_meetings

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

    def test_delete_meeting_button(self):
        meeting = Meeting(movie='Test Film', cafe='Coffee Testers', cafeAddress='321 Test Ave', time_of_meeting='12')
        meeting.save()

        