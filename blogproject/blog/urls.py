# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [

    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.about),
    url(r'^contact/$', views.contact),
    url(r'^full_width/$', views.full_width),
    url(r'^single/(?P<pk>[0-9]+)/$', views.single, name='single'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
]























