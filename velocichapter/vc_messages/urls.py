from django.conf.urls import url

from vc_messages import views

urlpatterns = [
    url(r'^$', views.messages_home, name='vc_messages'),
]
