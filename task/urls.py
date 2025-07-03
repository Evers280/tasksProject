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
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenRefreshView
from Users import views
from Users.views import CustomTokenObtainPairView, logout_master
from django.views.generic import TemplateView



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Endpoints d'APIs
    path('tasksMaster/', include('Tasks.urls')), 
    path('taskMasters/', include('Users.urls')),    
    
    # Login et Logout utilisant JWT
    path('tasksMasters/login/', CustomTokenObtainPairView.as_view(), name='tasksMasters_login'),
    path('tasksMasters/logout/', logout_master, name='tasksMasters_logout'),
    
    # Endpoints de Token
    path('tasksMasters/refresh_token/',  TokenRefreshView.as_view(), name='token_refresh'),
    path('tasksMasters/get_csrf_token/', views.get_csrf_token, name='get_csrf_token'),
    
    # Urls pour l'authentification sociale Allauth
    path('accounts/', include('allauth.urls')),
    
    # Urls pour reinitialiser le mot de passe
    path('tasksMasters/auth/', include('dj_rest_auth.urls')),    
    
    # URL fictive pour que `reverse('password_reset_confirm', ...)` fonctionne.
    # Cette URL est requise par django-allauth/dj-rest-auth pour générer le lien de réinitialisation.
    re_path(
        r'^tasksMasters/auth/password/reset/confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$',
        TemplateView.as_view(),
        name='password_reset_confirm'
    ),
    # Urls pour swagger
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]