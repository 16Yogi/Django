from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/all_lession
    # all_lession this is the function name
    path('',views.all_lession,name='all_lession'),   
    # path('lession1',views.all_lession,name='all_lession'),   

]