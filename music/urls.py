from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns = [
    # /music/ - Homepage
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/<album_id>/ - Album Details
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
]