"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^teams/$', views.teams, name='teams'),
    url(r'^users/$', views.users, name='users'),
    url(r'^teamprof/(?P<team_id>[0-9]+)$', views.teamprof, name = 'teamprof'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^userprof/(?P<user_id>[0-9]+)', views.userprof, name = 'userprof'),
    url(r'^hackprof/(?P<hackathon_id>[0-9]+)', views.hackprof, name = 'hackprof'),
    url(r'^teamEnroll/(?P<team_id>[0-9]+)$', views.teamEnroll, name = 'teamEnroll'),
    url(r'^like/(?P<project_id>[0-9]+)$', views.like, name = 'like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
