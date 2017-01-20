from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<trail_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<trail_id>[0-9]+)/like/$', views.like, name='like'),
    url(r'^(?P<trail_id>[0-9]+)/dislike/$', views.dislike, name='dislike'),
    url(r'^modify/(?P<trail_id>[0-9]+)/$', views.modify, name='modify'),
    #trail added handled in a template
    url(r'^dc/$', views.dc, name='dc'),
]
