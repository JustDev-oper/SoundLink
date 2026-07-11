from django.contrib.auth.models import User
from django.db import models


class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='playlists_covers/', blank=True, null=True)
    is_private = models.BooleanField(default=True)
    is_for_friends = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
