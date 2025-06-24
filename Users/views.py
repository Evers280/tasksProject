from rest_framework import viewsets
from .models import Masters
from .serializers import MastersSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser



class MasterViewSet(viewsets.ModelViewSet):
    queryset = Masters.objects.all()
    serializer_class = MastersSerializer
    
    def get_permissions(self):
        
        if self.action in ['create']:
            self.permission_classes = [AllowAny]
            
        elif self.action in ['list', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAdminUser]
            
        else:
            self.permission_classes = [IsAdminUser]
            
        return super().get_permissions()