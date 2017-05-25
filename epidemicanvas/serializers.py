from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Session, Artist


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'name', 'artist',)
        read_only_fields = ('id',)


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'first_name', 'last_name',)
        read_only_fields = ('id',)

        def create(self, validated_data):
            return Artist.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)

            instance.save()

            update_session_auth_hash(self.context.get('request'), instance)
            return instance
