from django.conf.urls import patterns, include, url
from django.contrib import admin
from preconsulta import urls
from userprofiles import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CREE.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^preconsulta/', include('preconsulta.urls')),
    url(r'^login/', include('userprofiles.urls')),
)
