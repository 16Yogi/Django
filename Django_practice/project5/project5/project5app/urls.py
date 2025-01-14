from . import views 
from django.urls import path  

urlpatterns = [
    path('',views.home,name='home'),
    path('registration/',views.registation,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('tweet_list/',views.tweet_list,name='tweet_list')
]
