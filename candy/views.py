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

class CategoryDetailView(generic.DetailView):
	model = Category

class ItemDetailView(generic.DetailView):
	model = Item

class CreateCategoryView(CreateView):
	#template_name is "candy/category_form.html"
	model = Category
	fields = ['category', 'name', 'description']

	def get_success_url(self):
		return reverse('candy:categorydetail', args=(self.object.pk,))

class UpdateCategoryView(UpdateView):
	#template_name is "candy/category_form.html"
	model = Category
	fields = ['category', 'name', 'description']

	def get_success_url(self):
		return reverse('candy:categorydetail', args=(self.object.pk,))

class DeleteCategoryView(DeleteView):
	#tempalte_name is "category_confirm_delete.html"
	model = Category
	success_url = reverse_lazy('candy:deletecategorysuccess')
	
class CreateItemView(CreateView):
	#template_name is "candy/item_form.html"
	model = Item
	fields = ['name', 'quantity', 'description', 'category']
	def get_success_url(self):
		return reverse('candy:categorydetail', args=(self.object.category.id,))

class UpdateItemView(UpdateView):
	#template_name is "candy/item_form.html"
	model = Item
	fields = ['name', 'quantity', 'description', 'category']

	def get_success_url(self):
		return reverse('candy:categorydetail', args=(self.object.category.id,))

class DeleteItemView(DeleteView):
	#tempalte_name is "item_confirm_delete.html"
	model = Item

	def get_success_url(self):
		return reverse('candy:categorydetail', args=(self.object.category.id,))
