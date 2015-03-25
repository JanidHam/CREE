from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CREE.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),
    url(r'^revision-medica/(?P<paciente>[\w\-]+)/$', views.revisionMedica, name='revision_medica'),
    url(r'^agregar-paciente/$', views.agregar_paciente, name='agrega_paciente'),
    url(r'^agregar-hoja-prevaloracion/$', views.addHojaPrevaloracion, name='agregar_hoja_prevaloracion'),
)