from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name="r_base"),
    path('chant/', views.chant, name="chant-home"),
    path('chant/<slug:category_slug>/', views.song_list, name="song_list"),
    path('chant/<slug:category_slug>/<slug:slug>/', views.song_detail, name="song_detail"),

    path('user/<slug:category_slug>/', views.update_category, name='update-category'),
]