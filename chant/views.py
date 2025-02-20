from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Song, Section, Line, Category, Language



#base view function
def base(request):
    return render(request, 'chant/base.html')


def song_list(request, category_slug):
    """ View to display the list of all songs"""
    selected_language = request.GET.get('choice', 'creole')
    #songs_in_selected_lang = Song.objects.filter(language__language_type=selected_language)
    category = Category.objects.get(slug = category_slug)
    songs = Song.objects.filter(language__language_type=selected_language, category=category).order_by("category_number")
    return render(request, 'chant/song_list.html', {'songs': songs, 'selected_language': selected_language})


def song_detail(request, category_slug, category_number):
    """ View to display a songle song with it's sections and lines """
    category = Category.objects.get(slug = category_slug)
    song = Song.objects.get(category_number=category_number)
    verse_counter = 0

    return render(request, 'chant/song_detail.html', {'song': song, 'verse_counter': verse_counter})


def home(request):
    return HttpResponse("<h1>Hello!!!</h1>")

def chant(request):
    """Returns list of Category"""
    categories = Category.objects.all()
    return render(request, 'chant/chant_home.html', {'categories': categories})
