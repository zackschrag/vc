from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vc.views.login', name='login'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('vc_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
