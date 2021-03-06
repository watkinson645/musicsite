from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.contrib.auth.views import LogoutView

app_name = "music"

urlpatterns = [
    # /music/ - Homepage
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/<album_id>/ - Album details
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),



    # /music/album/add/ - Create new album
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/<album_id>/ - Update album
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/<album_id>/delete/ - Delete album
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),



    # /music/register - Register an account
    url(r'^register/$', views.UserFormView.as_view(), name='signup'),

    # /music/login - Login to account
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),

    # /music/logout - Logout and redirect
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),



    # /music/song/add/ - Create new song
    url(r'song/add/$', views.SongCreate.as_view(), name='song-add'),

    # /music/song/<song_id>/ - Update song
    url(r'song/(?P<pk>[0-9]+)/$', views.SongUpdate.as_view(), name='song-update'),

    # /music/song/<song_id>/delete/ - Delete song
    url(r'song/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),



    # /music/all/ - View all albums in JSON (REST API)
    url(r'all/$', views.AlbumList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)