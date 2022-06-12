from django.urls import path
from . import views


urlpatterns = [
   
    path('uploads/', views.uploads, name='uploads'),
    path('uploads/upload', views.upload, name='upload'),
    path('post/<str:pk>/',views.view_post, name='viewpost'),
    path('projects/', views.projects, name='projects'),
    
    
]