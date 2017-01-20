from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^likeview/$', views.likeview, name='likeview'),
    url(r'^(?P<pic_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<pic_id>[0-9]+)/like/$', views.like, name='like'),
    url(r'^(?P<pic_id>[0-9]+)/dislike/$', views.dislike, name='dislike'),
    #url(r'^search/$', views.search, name='search'),
    url(r'^modify/(?P<pic_id>[0-9]+)/$', views.modify, name='modify'),
    #url(r'^reportadded/$', views.reportadded, name='reportadded'),
    #url(r'^commented/(?P<report_id>[0-9]+)/$', views.commented, name='commented'),
    #url(r'^liked/(?P<report_id>[0-9]+)/$', views.liked, name='liked'),
]


