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
    url(r'^deployment/$', views.DeploymentList.as_view()),
    url(r'^deployment/(?P<pk>[0-9]+)/$', views.DeploymentDetail.as_view()),
    url(r'^node/$', views.NodeList.as_view()),
    url(r'^node/(?P<pk>[0-9]+)/$', views.NodeDetail.as_view()),
    url(r'^confseq/$', views.ConfSeqList.as_view()),
    url(r'^confseq/(?P<pk>[0-9]+)/$', views.ConfSeqDetail.as_view()),
    url(r'^sensormap/$', views.SensorMapList.as_view()),
    url(r'^sensormap/(?P<pk>[0-9]+)/$', views.SensorMapDetail.as_view()),
    url(r'^sensor/$', views.SensorList.as_view()),
    url(r'^sensor/(?P<pk>[0-9]+)/$', views.SensorDetail.as_view()),
    url(r'^reading/$', views.ReadingList.as_view()),
    url(r'^reading/(?P<pk>[0-9]+)/$', views.ReadingDetail.as_view()),
    url(r'^statistics/$', views.StatisticsList.as_view()),
    url(r'^statistics/(?P<pk>[0-9]+)/$', views.StatisticsDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^admin/', include(admin.site.urls)),

)
# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
