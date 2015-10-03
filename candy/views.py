from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

from .models import Category, Item

# Create your views here.

class CategoryListView(generic.ListView):
	template_name = "candy/index.html"
	model = Category

class ItemListView(generic.ListView):
	template_name = "candy/item_list.html"
	model = Category

class ItemDetailView(generic.DetailView):
	template_name = "candy/item_detail.html"
	model = Item
