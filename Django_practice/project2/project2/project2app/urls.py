from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.allUser_view,name='alluser'),
    path('register/',views.register,name='register'),
    path('all-users/', views.regUsers, name='all_users'),
    # edit / update
    path('<int:project_id>/edit/',views.user_edit,name='editUser'),
    path('create/',views.create_update,name='create_update'),
]