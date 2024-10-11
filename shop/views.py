from django.shortcuts import render
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView,
                                DetailView, TemplateView)

from django.urls import reverse_lazy

from .models import Product, Category
from .forms import CategoryCreateForm, ProductCreateForm

class AdminTemplateView(TemplateView):
    template_name = 'shop/admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = 5
        return context


class ProductCreateView(CreateView):
    model = Product
    exclude = ['slug', 'created', 'updated']


class ProductListView(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    form_class = CategoryCreateForm
    template_name = 'shop/category_add.html'
    success_url = reverse_lazy('categories')


class CategoryListView(ListView):
    model = Category
    template_name = 'shop/categories.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'
    context_object_name = 'category'
    slug_url_kwarg = 'slug'
