from django.conf.urls import url

from vc_auth import views

urlpatterns = [
    url(r'^$', 'vc_auth.views.login', name='login'),
]
