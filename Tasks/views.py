from rest_framework import viewsets
from .models import Tasks
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser



class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    
    def get_permissions(self):
        
        if self.action in ['create', 'list', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAdminUser]
            
        else:
            self.permission_classes = [IsAdminUser]
            
        return super().get_permissions()