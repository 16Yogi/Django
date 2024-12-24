from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_lession,name="all_lession"),
    path('app_about/',views.app_about,name="app_about"),
    path('app_contact/',views.app_contact,name="app_contact"),
    path('<int:lession_id>/',views.lession_details,name='lession_details')
]