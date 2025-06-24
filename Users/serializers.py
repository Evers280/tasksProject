from rest_framework import serializers
from .models import Masters

class MastersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masters
        fields = '__all__'