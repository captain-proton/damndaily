from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<damndailyid>[a-zA-Z0-9]+)/$', views.view, name='view'),
    url(r'^(?P<damndailyid>[a-zA-Z0-9]+)/edit/$',
        views.edit, name='edit'),
]
