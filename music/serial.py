from rest_framework import serializers
from .models import Album

class AlbumSerial(serializers.ModelSerializer):

    class Meta:
        model = Album

        # fields = '__all__'
        fields = ('artist', 'title')