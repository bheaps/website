from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /reports/5/
    url(r'^(?P<report_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create, name='create'),
    url(r'^create2/$', views.reportsparticipants, name='reportsparticipants'),
    url(r'^addparticipants/$', views.addparticipants, name='addparticipants'),
    url(r'^(?P<report_id>[0-9]+)/like/$', views.like, name='like'),
    url(r'^(?P<report_id>[0-9]+)/dislike/$', views.dislike, name='dislike'),
    url(r'^deleteparticipant/(?P<part_id>[0-9]+)/$', views.deleteparticipant, name='deleteparticipant'),
    url(r'^modify/(?P<report_id>[0-9]+)/$', views.modify, name='modify'),
    url(r'^modifyparticipants/(?P<report_id>[0-9]+)/$', views.modifyparticipants, name='modifyparticipants'),
    url(r'^deleteparticipantmodify/(?P<part_id>[0-9]+)/(?P<report_id>[0-9]+)/$', views.deleteparticipantmodify, name='deleteparticipantmodify'),
    url(r'^reportadded/$', views.reportadded, name='reportadded'),
    url(r'^commented/(?P<report_id>[0-9]+)/$', views.commented, name='commented'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    #url(r'^liked/(?P<report_id>[0-9]+)/$', views.liked, name='liked'),
    url(r'^dc/$', views.dc, name='dc'),
]


