from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

from .models import Category, Item

# Create your views here.

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = model_to_dict(self.object)
            return JsonResponse(data)
        else:
            return response

class CategoryListView(ListView):
	template_name = "candy/index.html"
	model = Category

class CategoryDetailView(DetailView):
	model = Category

	def render_to_response(self, context, **kwargs):
		if self.request.is_ajax():
			return JsonResponse(serializers.serialize('json', self.object))
		return super(CategoryDetailView, self).render_to_response(context, **kwargs)

class ItemDetailView(DetailView):
	model = Item

	def render_to_response(self, context, **kwargs):
		if self.request.is_ajax():
			return JsonResponse(serializers.serialize('json', self.object))
		return super(ItemDetailView, self).render_to_response(context, **kwargs)

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
		return reverse_lazy('candy:categorydetail', args=(self.object.category.id,))

class UpdateItemView(AjaxableResponseMixin, UpdateView):
	#template_name is "candy/item_form.html"
	model = Item
	fields = ['name', 'quantity', 'description', 'category']

	def get_success_url(self):
		return reverse_lazy('candy:categorydetail', args=(self.object.category.id,))

class UpdateItemQuantityView(AjaxableResponseMixin, UpdateView):
    model = Item
    fields = ['quantity']

    def get_success_url(self):
        return reverse_lazy('candy:categorydetail', args=(self.object.category.id,))

class DeleteItemView(DeleteView):
	#tempalte_name is "item_confirm_delete.html"
	model = Item

	def get_success_url(self):
		return reverse('candy:categorydetail', args=(self.object.category.id,))
