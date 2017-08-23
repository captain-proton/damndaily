from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<damndailyid>[a-zA-Z0-9]+)/$', views.view, name='view'),
]
