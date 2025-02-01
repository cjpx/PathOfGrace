from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name="r_base"),
    path('chant/', views.chant_home, name="chant-home"),
    path('chant/song/', views.song_list, name="song_list"),
    path('song/<int:song_id>/', views.song_detail, name="song_detail")
]