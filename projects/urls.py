from django.urls import path,re_path
from . import views


urlpatterns = [
   
    path('uploads/', views.uploads, name='uploads'),
    path('uploads/upload', views.upload, name='upload'),
    path('post/<str:pk>/',views.view_post, name='viewpost'),
    path('projects/', views.projects, name='projects'),
    path('<pk>/rate', views.Rate, name='rate-project'),
    path('search', views.search, name='search'),
    path('api/projects/', views.ProjectList.as_view()),
    
    
]