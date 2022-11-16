from django.urls import path
from . import views_tmdb
from . import views

urlpatterns = [
    path('', views.movies_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('tmdb/', views_tmdb.tmdb_data),
]
