from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Song, Section, Line



#base view function
def base(request):
    return render(request, 'chant/base.html')

# List of songs (with verses and choruses) in the desired format

def song_list(request):
    """ View to display the list of all songs"""
    songs = Song.objects.all()
    return render(request, 'chant/song_list.html', {'songs': songs})


def song_detail(request, song_id):
    """ View to display a songle song with it's sections and lines """
    song = get_object_or_404(Song, id=song_id)

    return render(request, 'chant/song_detail.html', {'song': song})


def home(request):
    return HttpResponse("<h1>Hello!!!</h1>")
