from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.CategoryListView.as_view(), name='index'),
	url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetailView.as_view(), name='categorydetail'),
	url(r'^item/(?P<pk>[0-9]+)/$', views.ItemDetailView.as_view(), name='itemdetail'),
]
