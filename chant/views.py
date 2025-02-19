from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Song, Section, Line, Category, Language



#base view function
def base(request):
    return render(request, 'chant/base.html')


def song_list(request, category_name):
    """ View to display the list of all songs"""
    songs = Song.objects.filter(category_id = category_name).order_by('category_number')
    return render(request, 'chant/song_list.html', {'songs': songs})


def song_detail(request, category_number):
    """ View to display a songle song with it's sections and lines """
    song = Song.objects.get(category_number=category_number)
    verse_counter = 0

    return render(request, 'chant/song_detail.html', {'song': song, 'verse_counter': verse_counter})


def home(request):
    return HttpResponse("<h1>Hello!!!</h1>")

def chant(request):
    """Returns list of Category"""
    categories = Category.objects.all()
    return render(request, 'chant/chant_home.html', {'categories': categories})
