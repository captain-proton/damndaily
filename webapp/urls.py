from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^save/$', views.save_damn_daily, name='save_damn_daily'),

    url(r'^(?P<damndailyid>[a-zA-Z0-9]+)/$', views.view, name='view'),
    url(r'^(?P<damndailyid>[a-zA-Z0-9]+)/partake/$',
        views.partake, name='partake'),

    url(r'^(?P<todayid>[a-zA-Z0-9]+)/update_today/$',
        views.update_today, name='update_today'),
]
