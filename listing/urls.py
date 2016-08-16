from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^(?P<listing_id>[0-9]+)/$', views.list_detail, name='list_detail'),
		url(r'^search/', views.get_search, name='get_search'),
		url(r'^submit/', views.get_submit, name='get_submit'),
]
