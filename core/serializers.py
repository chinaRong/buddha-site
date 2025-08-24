from rest_framework import serializers
from .models import BackgroundImage, MusicTrack, Quote

class BackgroundImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundImage
        fields = ["id", "title", "image"]

class MusicTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicTrack
        fields = ["id", "title", "audio"]

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ["id", "text", "author", "source", "language"]
