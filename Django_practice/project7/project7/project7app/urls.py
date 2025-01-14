from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('reg1_user_list/',views.reg1_user_list, name='reg1_user_list'), 
    path('reg2_user_list/',views.reg2_user_list, name='reg2_user_list'),
    path('registration/',views.registration1,name='reg1'),
    path('registration2/',views.registertion2,name='reg2'),
    path('adminreg/',views.adminReg,name='adminreg'),
    path('<int:user_id>/edit/',views.edit_registration1,name='reg1Edit'),
]
