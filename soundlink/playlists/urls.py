from django.urls import path

from .views import PlaylistCreateView, PlaylistsView, PlaylistDeleteView

...

urlpatterns = [
    path("playlists/create/", PlaylistCreateView.as_view(), name="playlist-create"),
    path("playlists/delete/", PlaylistDeleteView.as_view(), name="playlist-delete"),
    path("playlists/", PlaylistsView.as_view(), name="playlists-list"),
]
