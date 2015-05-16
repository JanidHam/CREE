from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CREE.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),
    
    url(r'^revision-medica/(?P<paciente>[\w\-]+)/$', views.revisionMedica, name='revision_medica'),
    url(r'^revision-psicologica/(?P<paciente>[\w\-]+)/$', views.psicologicaPrevaloracion, name='revision_psicologica'),
    url(r'^revision-estudio-socioeconomico/(?P<paciente>[\w\-]+)/$', views.estudioSPrevaloracion, name='revision_estudio_socioeconomico'),
    url(r'^enfermeria/(?P<paciente>[\w\-]+)/$', views.enfermeriaPrevaloracion, name='enfermeria_prevaloracion'),
    url(r'^imprimir-documentos/(?P<paciente>[\w\-]+)/$', views.imprimirDocumentos, name='imprimir_documentos'),

    url(r'^agregar-paciente/$', views.agregar_paciente, name='agrega_paciente'),
    url(r'^agregar-enfermeria/$', views.addDataEnfermeria, name='agrega_enfermeria'),
    url(r'^agregar-hoja-prevaloracion/$', views.addHojaPrevaloracion, name='agregar_hoja_prevaloracion'),
    url(r'^agregar-hoja-prevaloracion-psicologia/$', views.addPsicologiaHojaPrevaloracion, name='agregar_hoja_prevaloracion_psicologica'),
    url(r'^agregar-estudio-socio-economico/$', views.addEstudioSocioeconomico, name='agregar_hoja_prevaloracion_estudio_socioeconomico'),
)