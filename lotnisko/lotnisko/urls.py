from django.conf.urls import patterns, include, url
from django.contrib import admin
from table import views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexFlights.as_view(), name='index'),
)
