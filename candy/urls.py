from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.CategoryListView.as_view(), name='index'),
	url(r'^category/(?P<pl>[0-9]+)/$', views.ItemListView.as_view(), name='item_list'),
	url(r'^category/(?P<pk>[0-9]+)/item/(?P<pk>[0-9]+/$', views.ItemDetailView.as_view(), name='item_detail'),
]
