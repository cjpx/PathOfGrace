from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name="r_base"),
    path('chant/', views.chant, name="chant-home"),
    path('chant/<str:category_name>/', views.song_list, name="song_list"),
    path('chant/song/<int:category_number>/', views.song_detail, name="song_detail")
]