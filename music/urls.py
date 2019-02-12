from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/ - Homepage
    url(r'^$', views.index, name='index'),

    # /music/712/ - Album Details
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
]