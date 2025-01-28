from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="chant-index"),
    path('chant/', views.home, name="chant-home"),
    path('about/', views.about, name="chant-about"),
]