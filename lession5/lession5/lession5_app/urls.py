from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_app,name='home'),  
    path('app_about/',views.app_about,name='about'),
    # path('<int:lession_id>',views.lession_detaion,name='lessionDetailes'),
    # path('lession_dtl/',views.lession_details,name='lession')
    path('<int:lession_id>/', views.lession_details, name='lession_detail'),
    

]