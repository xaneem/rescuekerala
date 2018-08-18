from rest_framework import serializers

from .models import RescueCamp, Person

class RescueCampSerializer(serializers.ModelSerializer):
    class Meta:
        model = RescueCamp
        fields = '__all__'

class RescueCampShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = RescueCamp
        fields = ('id', 'name', 'district')


class PersonSerializer(serializers.ModelSerializer):

	class Meta:
		model = Person
		fields = '__all__'


class CampListSerializer(serializers.Serializer):
	district = serializers.CharField()