from django.urls import path
from . import views_tmdb
from . import views

urlpatterns = [
    path('', views.movies_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/comment_create/', views.comment_create),
    path('commentlist/', views.comment_list),
    path('<int:comment_pk>/comment_detail/', views.comment_detail),
    path('<int:movie_pk>/<int:user_pk>/likes/', views.likes),
    path('tmdb/', views_tmdb.tmdb_data),
]
