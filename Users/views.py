from rest_framework import viewsets
from .models import Masters
from .serializers import MastersSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from django.http import JsonResponse

from django.middleware.csrf import get_token

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken


def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        user = serializer.user
        response_data = serializer.validated_data

        user_data = {
            'id': user.id,
            'email': user.email,
            'password': user.password,

        }
        response_data['user'] = user_data
        response_data['message'] = "Connexion réussie !"

        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_master(request):
    try:
        # Récupérer le refresh token envoyé dans le corps de la requête
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({"error": "Le refresh_token est requis !"}, status=status.HTTP_400_BAD_REQUEST)

        # Ajouter le refresh token à la liste noire
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({"message": "Déconnexion réussie !"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": f"Erreur lors de la déconnexion : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)




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