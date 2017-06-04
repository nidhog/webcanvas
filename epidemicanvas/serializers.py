from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Session, Artist, Contributions
from .fields import ImageBase64Field


class SessionSerializer(serializers.ModelSerializer):
    image = ImageBase64Field(
        max_length=None, use_url=True, default=None
    )
    print('YOLO')

    def create(self, validated_data):
        print(validated_data)
        print('TODOh---------------------')
        print('TODOh---------------------')
        print('TODOh---------------------')
        print('TODOh---------------------')
        return super(SessionSerializer, self).create(validated_data)

    class Meta:
        model = Session
        fields = ('id', 'name', 'artist', 'image')
        read_only_fields = ('id',)


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'email', 'first_name', 'last_name',)
        read_only_fields = ('id',)

        def create(self, validated_data):
            return Artist.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.email = validated_data.get('email', instance.email)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)

            instance.save()

            update_session_auth_hash(self.context.get('request'), instance)
            return instance


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributions
        fields = ('id', 'session', 'artist', 'image', 'created','updated')
        read_only_fields = ('id',)
