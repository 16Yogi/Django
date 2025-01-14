from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.movie_list,name='index'),
    path('registration/',views.registration,name='registration'),
    path('uploadmovie/',views.movie_create,name='uploadmovie'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('allUser/',views.allUser,name='all_user'),
    path('testuser/',views.testfrom,name='testuser')
]

