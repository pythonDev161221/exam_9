from rest_framework import serializers

from webapp.models import Photo, User


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("id", "photo", "signature", "created_at", "author", "album", "private", "choose")
        read_only_fields = ("id", "photo", "signature", "created_at", "author", "album", "private")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "choose_photos", "choose_albums")
        read_only_fields = ("id", "name")
