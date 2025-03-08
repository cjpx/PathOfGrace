from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Song, Section, Line, Category, Language
from .forms import CategoryForm
from users.models import Profile



#base view function
def base(request):
    user = User
    return render(request, 'chant/base.html', {'user': user})


def song_list(request, category_slug):
    """ View to display the list of all songs"""
    selected_language = request.GET.get('choice', 'Créole')
    #songs_in_selected_lang = Song.objects.filter(language__language_type=selected_language)
    category = Category.objects.get(slug = category_slug)
    songs = Song.objects.filter(language__language_type=selected_language, category=category).order_by("category_number")
    return render(request, 'chant/song_list.html', {'songs': songs, 'selected_language': selected_language, 'category': category})


def song_detail(request, category_slug, slug):
    """ View to display a songle song with it's sections and lines """
    category = Category.objects.get(slug = category_slug)
    song = Song.objects.get(slug=slug, category=category)
    verse_counter = 0

    return render(request, 'chant/song_detail.html', {'song': song, 'verse_counter': verse_counter})


def chant(request):
    """Returns list of Category"""
    categories = Category.objects.all()
    #context = {'categories': categories}
    return render(request, 'chant/chant_home.html', {'categories': categories})

def update_category(request, category_slug):
    category = Category.objects.get(slug = category_slug)
    form  = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('chant-home')
    
    
    return render(request, 'chant/cat_form.html', {'category': category, 'form': form})
