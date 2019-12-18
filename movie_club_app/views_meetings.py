from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import NewMeetingForm
from .models import Meeting

@login_required
def new_meeting(request):
    if request.method == 'POST':
        form = NewMeetingForm(request.POST, request.FILES, instance=None)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.save()
            return redirect('movie_club_app:meeting_list')
    
    else :
        form = NewMeetingForm()

    return render(request, 'movie_club_app/meetings/create_new_meeting.html' , { 'form' : form })

def meeting_list(request):
    meetings = Meeting.objects.all().order_by('time_of_meeting').reverse()
    return render(request, 'movie_club_app/meetings/meeting_list.html', {'meetings':meetings})

def meeting_details(request, meeting_pk):
    meeting = get_object_or_404(Meeting, pk=meeting_pk)
    return render(request, 'movie_club_app/meetings/meeting_page.html' , {'meeting' : meeting })

@login_required
def delete_meeting(request, meeting_pk):
    meeting = get_object_or_404(Meeting, pk=meeting_pk)
    meeting.delete()
    return redirect('movie_club_app:meeting_list')