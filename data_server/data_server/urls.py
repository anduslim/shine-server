from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from data_server import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^deployment/$', views.DeploymentList.as_view(), name='deployment-list'),
    url(r'^deployment/(?P<pk>[0-9]+)/$', views.DeploymentDetail.as_view(), name='deployment-detail'),
    url(r'^node/$', views.NodeList.as_view(), name='node-list'),
    url(r'^node/(?P<pk>[0-9]+)/$', views.NodeDetail.as_view(), name='node-detail'),
    url(r'^confseq/$', views.ConfSeqList.as_view(), name='confseq-list'),
    url(r'^confseq/(?P<pk>[0-9]+)/$', views.ConfSeqDetail.as_view(), name='confseq-detail'),
    url(r'^sensormap/$', views.SensorMapList.as_view(), name='sensormap-list'),
    url(r'^sensormap/(?P<pk>[0-9]+)/$', views.SensorMapDetail.as_view(), name='sensormap-detail'),
    url(r'^sensor/$', views.SensorList.as_view(), name='sensor-list'),
    url(r'^sensor/(?P<pk>[0-9]+)/$', views.SensorDetail.as_view(), name='sensor-detail'),
    url(r'^reading/$', views.ReadingList.as_view(), name='reading-list'),
    url(r'^reading/(?P<pk>[0-9]+)/$', views.ReadingDetail.as_view(), name='reading-detail'),
    url(r'^statistics/$', views.StatisticsList.as_view(), name='statistics-list'),
    url(r'^statistics/(?P<pk>[0-9]+)/$', views.StatisticsDetail.as_view(), name='statistics-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
