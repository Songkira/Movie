from django.urls import path, include
from . import views

urlpatterns = [
   path('signup/', views.signup),
   path('<int:my_pk>/<int:person_pk>/follow/', views.follow),
   path('<int:my_pk>/', views.myinfo),
   path('<int:person_pk>/followinfo/', views.followinfo),
   path('usersinfo/', views.usersinfo),
   path('<int:person_pk>/likeslist/', views.userlikelist),
]
