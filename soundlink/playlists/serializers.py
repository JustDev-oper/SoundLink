from rest_framework import serializers

from soundlink.playlists.models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('id', 'title', 'description', 'is_private', 'is_for_friends', 'cover')
        read_only_fields = ('user', 'created_at')
