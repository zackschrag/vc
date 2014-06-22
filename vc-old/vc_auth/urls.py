from django.conf.urls import url

from vc_auth import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^index', 'vc_auth.views.index', name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^register_chapter/', views.register_chapter, name='register_chapter'),
]
