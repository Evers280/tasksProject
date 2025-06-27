from rest_framework import viewsets
from .models import Tasks
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import AnonymousUser 


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        """
        Cette vue doit retourner les tâches de l'utilisateur connecté.
        Si l'utilisateur est un administrateur (is_staff), elle retourne toutes les tâches.
        """
        user = self.request.user
        if user.is_authenticated and not isinstance(user, AnonymousUser):
            if user.is_staff:
                return Tasks.objects.all()
            return Tasks.objects.filter(masters=user)
        # Pour les utilisateurs non authentifiés, retourner un queryset vide.
        return Tasks.objects.none()
    
    def get_permissions(self):
        
        if self.action in ['create', 'list', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated]
            
        else:
            self.permission_classes = [IsAdminUser]
            
        return super().get_permissions()