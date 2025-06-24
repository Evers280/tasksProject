from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MasterViewSet

router = DefaultRouter()
router.register(r'masters', MasterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
