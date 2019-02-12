from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns = [
    # /music/ - Homepage
    url(r'^$', views.index, name='index'),

    # /music/<album_id>/ - Album Details
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
]