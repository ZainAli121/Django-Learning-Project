from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('create-project/', views.createProject, name='create-project'),
    path('update-project/<str:pk>/', views.updateProject, name='update-Project'),
    path('delete-project/<str:pk>/', views.deleteProject, name='delete-Project'),
    path('signup/', views.signupUser, name='signupUser'),
    path('login/', views.loginUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('profile/<str:pk>/', views.devProfile, name='profile'),
    path('update-profile/<str:pk>/', views.updateProfile, name='update-profile'),
    path('developers/', views.developers, name='developers'),
    path('inbox/', views.inbox, name='inbox'),
    
]
