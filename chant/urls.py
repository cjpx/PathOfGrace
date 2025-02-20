from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name="r_base"),
    path('chant/', views.chant, name="chant-home"),
    path('chant/<slug:category_slug>/', views.song_list, name="song_list"),
    path('chant/<slug:category_slug>/<int:category_number>/', views.song_detail, name="song_detail")
]