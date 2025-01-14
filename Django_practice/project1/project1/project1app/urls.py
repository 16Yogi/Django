from django.urls import path,include
from . import views

urlpatterns = [
    # path('', views.index,name='index'),
    path('project/',views.project_list,name='project_list'),
    path('create/',views.project_create, name='project_create'),
    # path('<int:project_id>/edit/',views.project_edit, name='project_edit'),
    path('<int:project_id>/edit/', views.project_edit, name='project_edit'),
    path('<int:project_id>/delete/',views.project_delete, name='project_delete'),
    path('register/',views.register, name='register'),

]