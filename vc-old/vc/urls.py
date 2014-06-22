from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vc.views.login', name='login'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'vc.views.index', name='index'),
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^home/', 'vc.views.home', name='home'),
    url(r'^register/', 'vc.views.register', name='register'),
    url(r'^vc_auth/', include('vc_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
