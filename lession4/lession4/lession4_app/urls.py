from django.urls import path
from . import views

urlpatterns = [
    path('',views.lession4_all,name="home"),
    path('lession4_about/',views.lession4_about,name="about"),
    path('lession4_contact/',views.lession4_contact,name="contact")
]