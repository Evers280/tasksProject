from rest_framework import serializers
from .models import Tasks
from django.db.utils import IntegrityError



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__' # Inclut tous les champs du modèle
        read_only_fields = ['id', 'masters'] # Rend 'id' et 'masters' en lecture seule

    def create(self, validated_data):
        try:
            task = Tasks.objects.create(
                titre=validated_data['titre'],
                description=validated_data['description'],
                date_echeance=validated_data['date_echeance'],
                priorite=validated_data['priorite'],
                status=validated_data['status'],
                # Le champ 'masters' est maintenant géré par perform_create dans le ViewSet
            )
            return task
        except IntegrityError:
            raise serializers.ValidationError(
                {'titre': 'Ce titre est déjà utilisé.'}
            )
