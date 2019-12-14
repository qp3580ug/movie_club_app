from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import NewMeetingForm
from django.utils import timezone

@login_required
def new_meeting(request):
    if request.method == 'POST':
        form = NewMeetingForm(request.POST, request.FILES, instance=None)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.save()
            return redirect('movie_club_app:meeting_page', meeting_pk=meeting.pk)
    
    else :
        form = NewMeetingForm()