from rest_framework import serializers
from music_review_app.models import Artists

class ArtistsSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 200)
    profile = serializers.CharField()
    date_of_birth = serializers.DateField(required = False)

class Meta:

    fields = ['id', 'name', 'profile', 'date_of_birth']

def create(self, validated_data):
    return ArtistsSerializer.objects.create(**validated_data)

def update(self, instance, validated_data):
    instance.name = validated_data.get("name", instance.name)
    instance.profile = validated_data.get("profile", instance.profile)
    instance.save()
    return instance


    