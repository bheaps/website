"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include,url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^trails/', include('trails.urls')),
    url(r'^reports/', include('reports.urls')),
    url(r'^imageotd/', include('imageotd.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('userprofile.urls')),

    #user auth urls
    url(r'^accounts/login/$', views.login, name="login"),
    url(r'^accounts/auth/$', views.auth_view, name="auth_view"),
    url(r'^accounts/logout/$', views.logout, name="logout"),
    url(r'^accounts/loggedin/$', views.loggedin, name="loggedin"),
    url(r'^accounts/invalid/$', views.invalid_login, name="invalid_login"),

    url(r'^accounts/register/$', views.register_user, name="register_user"),   
    url(r'^accounts/register_success/$', views.register_success, name="register_success"),
    url(r'^search/', include('haystack.urls')), 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
