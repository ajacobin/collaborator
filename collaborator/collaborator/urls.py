"""collaborator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin

from collab.views import StudentCreateView, StudentDetailView, SamiDashboardView, \
    ProjectCreate, ProjectAssign, ProjectDetailView, ProjectListView, EmailMessage

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', StudentCreateView.as_view(), name='student-create'),
    url(r'^students/(?P<pk>[0-9]+)/$', StudentDetailView.as_view(), name='student-detail'),
    url(r'^sami/dashboard/$', SamiDashboardView.as_view(), name='sami-dash'),
    url(r'^projects/create/$', ProjectCreate, name='project-create'),
    url(r'^projects/assign/$', ProjectAssign, name='project-assign'),
    url(r'^projects/list/$', ProjectListView.as_view(), name='project-list'),
    url(r'^projects/(?P<pk>[0-9]+)/msg/$', EmailMessage, name='email-project'),
    url(r'^projects/(?P<pk>[0-9]+)/$', ProjectDetailView.as_view(), name='project-detail'),
]
