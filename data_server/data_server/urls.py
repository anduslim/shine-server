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

router = routers.DefaultRouter()
router.register(r'nodes', views.NodeViewSet)



urlpatterns = [
    url(r'^deployments/$', views.DeploymentList.as_view()),
    url(r'^deployments/(?P<pk>[0-9]+)/$', views.DeploymentDetail.as_view()),
    url(r'^nodes/$', views.node_list),
    url(r'^nodes/(?P<pk>[0-9]+)/$', views.node_detail),
    url(r'^confseq/$', views.confseq_list),
    url(r'^confseq/(?P<pk>[0-9]+)/$', views.confseq_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'data_server.views.home', name='home'),
    # url(r'^data_server/', include('data_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),

)
# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
