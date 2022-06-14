from django.urls import path
from . import views



urlpatterns = [
    path('', views.landing, name='landing'),  
    path('signup/', views.signup, name='signup'),
    path('settings/', views.settings, name='settings'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:pk>', views.profile, name='profile'), 
    path('api/profile/', views.ProfileList.as_view()),
    
]