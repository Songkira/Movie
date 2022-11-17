from django.urls import path, include
from . import views

urlpatterns = [
   path('signup/', views.signup),
   path('<int:my_pk>/<int:person_pk>/follow/', views.follow),
   # path('<int:person_pk>/followcnt/', views.follow_count),
   path('usersinfo/', views.usersinfo),
]
