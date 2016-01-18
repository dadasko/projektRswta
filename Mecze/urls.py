from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
	url(r'^teams$', views.teams),
	url(r'^strzelcy$', views.strzelcy),
	url(r'^tabela$', views.tabela),
	url(r'^teams/(?P<druzyna>[0-9]+)/$', views.team_detail),
	url(r'^mecz/(?P<mecz>[0-9]+)/$', views.mecz),
]