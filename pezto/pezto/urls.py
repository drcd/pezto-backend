"""pezto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, patterns, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^paste$', 'pastes.views.post_paste', name='post_paste'),
    url(r'^paste/(?P<paste_uid>[A-Za-z0-9]+)$', 'pastes.views.get_paste', name='get_paste_by_uid'),
    
    # Raw
    url(r'^paste/(?P<paste_uid>[A-Za-z0-9]+)/raw$', 'pastes.views.get_paste_raw', name='get_paste_by_uid_raw'),
    url(r'^paste/(?P<paste_uid>[A-Za-z0-9]+).txt$', 'pastes.views.get_paste_raw', name='get_paste_by_uid_raw'),
]
