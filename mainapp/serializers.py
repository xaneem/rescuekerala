from rest_framework import serializers

from .models import RescueCamp

class RescueCampSerializer(serializers.ModelSerializer):
    class Meta:
        model = RescueCamp
        fields = '__all__'