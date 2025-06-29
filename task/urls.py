"""
URL configuration for task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from Users import views
from Users.views import CustomTokenObtainPairView, logout_master


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #endpoints d'APIs
    path('tasksMaster/', include('Tasks.urls')), 
    path('taskMasters/', include('Users.urls')),    
    
    # Login et Logout utilisant JWT
    path('tasksMasters/login/', CustomTokenObtainPairView.as_view(), name='tasksMasters_login'),
    path('tasksMasters/logout/', logout_master, name='tasksMasters_logout'),
    
    #endpoints de Token
    path('tasksMasters/refresh_token/',  TokenRefreshView.as_view(), name='token_refresh'),
    path('tasksMasters/get_csrf_token/', views.get_csrf_token, name='get_csrf_token'),
    
    # Urls pour l'authentification sociale Allauth
    path('accounts/', include('allauth.urls')),
]