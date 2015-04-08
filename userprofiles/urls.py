from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CREE.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
)