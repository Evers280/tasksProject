from rest_framework import viewsets
from .models import Masters
from .serializers import MastersSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser



class MasterViewSet(viewsets.ModelViewSet):
    queryset = Masters.objects.all()
    serializer_class = MastersSerializer
    
    def get_queryset(self):
        """
        Cette vue ne doit retourner que les informations de l'utilisateur
        connecté, sauf si c'est un administrateur (is_staff),
        auquel cas elle retourne tous les utilisateurs.
        """
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff:
                return Masters.objects.all()
            return Masters.objects.filter(pk=user.pk)
        # Pour les utilisateurs anonymes, retourner un queryset vide.
        return Masters.objects.none()
    
    
    
    def get_permissions(self):
        
        if self.action == 'create':
            self.permission_classes = [AllowAny]
            
        elif self.action in ['list', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated]
            
        else:
            self.permission_classes = [IsAdminUser]
            
        return super().get_permissions()