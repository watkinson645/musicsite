from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "music"

urlpatterns = [
    # /music/ - Homepage
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/<album_id>/ - Album details
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    # /music/album/add/ - Create new album
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2/ - Update album
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete/ - Delete album
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/register - Register an account
    url(r'^register/$', views.UserFormView.as_view(), name='signup'),

    # /music/all/ - View all albums in JSON (REST API)
    url(r'all/$', views.AlbumList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)