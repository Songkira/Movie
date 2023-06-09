from django.urls import path
from . import views_tmdb
from . import views

urlpatterns = [
    path('', views.movies_list),
    # path('genres/', views.genres_list),
    path('states/', views.state_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/comment_create/', views.comment_create),
    path('<int:movie_pk>/star_test/', views.star_test),
    path('<int:movie_pk>/starinfo/', views.starinfo),
    path('movie_comment/<int:movie_pk>/', views.comment_list),
    # path('movie_comment/<int:movie_pk>/<int:comment_pk>/', views.comment_delete),
    path('<int:comment_pk>/comment_detail/', views.comment_detail),
    path('<int:movie_pk>/<int:user_pk>/likes/', views.likes),
    path('<int:person_pk>/likemovies/', views.likemovies),
    path('<int:person_pk>/mycomments/', views.mycomments),
    path('<int:movie_pk>/<int:my_pk>/reviews/', views.review),
    path('<int:my_pk>/reviews/', views.reviewget),
    path('tmdb/', views_tmdb.tmdb_data),
]
