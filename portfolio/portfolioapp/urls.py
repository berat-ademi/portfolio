from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.createProject, name="create_project"),
    path('dashboard/<str:id>/', views.updateProject, name="update_project"),
    path('delete_project/<str:id>/', views.deleteProject, name="delete_project"),

    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    
]