from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views, account, auth

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^save/$', views.save_damn_daily, name='save_damn_daily'),

    url(r'^daily/(?P<damndailyid>[a-zA-Z0-9]+)/$', views.view, name='view'),
    url(r'^daily/(?P<damndailyid>[a-zA-Z0-9]+)/subscribe/$',
        views.subscribe, name='subscribe'),
    url(r'^daily/(?P<damndailyid>[a-zA-Z0-9]+)/save_subscription/$',
        views.save_subscription, name='save_subscription'),
    url(r'daily/(?P<damndailyid>[a-zA-Z0-9]+)/unsubscribe/$',
        views.unsubscribe, name='unsubscribe'),

    url(r'^today/(?P<todayid>[a-zA-Z0-9]+)/$',
        views.TodayDetailView.as_view(), name='today'),
    url(r'^today/(?P<todayid>[a-zA-Z0-9]+)/update_today/$',
        views.update_today, name='update_today'),

    url(r'^today/(?P<todayid>[a-zA-Z0-9]+)/participate/$',
        views.participate, name='participate'),
    url(r'^today/(?P<todayid>[a-zA-Z0-9]+)/reject/$',
        views.reject, name='reject'),

    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^reset_password/$', auth.reset_password, name='reset_password'),
    url(r'^register/$', auth.register, name='register'),
    url(r'^accounts/profile/$', account.profile, name='profile'),
    url('^', include('django.contrib.auth.urls')),
]
