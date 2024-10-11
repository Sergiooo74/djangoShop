from django.shortcuts import render
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView,
                                    DetailView)

from django.urls import reverse_lazy

from .models import Product, Category

class ProductListView(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    form_class = CategoryCreateForm
    template_name = 'shop/category_add.html'
    success_url = reverse_lazy('categories')

