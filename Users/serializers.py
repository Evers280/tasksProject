from rest_framework import serializers
from .models import Masters
from django.db.utils import IntegrityError

class MastersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masters
        fields = ['id', 'email', 'password']
        # Le mot de passe ne doit être accessible qu'en écriture (lors de la création ou mise à jour)
        # et ne doit jamais être retourné lors de la lecture des données de l'utilisateur.
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Crée et retourne un nouvel utilisateur Masters avec un mot de passe haché.
        """
        try:
            # Utilise **validated_data pour passer les arguments email et password directement
            user = Masters.objects.create_user(**validated_data)
            return user
        except IntegrityError:
            raise serializers.ValidationError(
                {'email': 'Cette adresse e-mail est déjà utilisée.'}
            )

    def update(self, instance, validated_data):
        try:
            instance.email = validated_data.get('email', instance.email)
            if 'password' in validated_data:
                instance.set_password(validated_data['password'])
            instance.save()
            return instance
        except IntegrityError:
            raise serializers.ValidationError(
                {'email': 'Cette adresse e-mail est déjà utilisée.'}
            )