from django.conf.urls import patterns, include, url
from velocichapter.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'velocichapter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'velocichapter.views.main_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^messages/', include('vc_messages.urls')),

    url(r'^login/', 'velocichapter.views.user_login'), #'django.contrib.auth.views.login'),
    url(r'^logout/$', 'velocichapter.views.logout_page'),
)
