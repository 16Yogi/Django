from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard_view,name='dashboad'),
    path('register/',views.registration_view,name='registration'),
    path('user_list/',views.user_list,name='user_list'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
]
