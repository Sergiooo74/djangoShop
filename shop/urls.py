from django.urls import path
from .views import (ProductListView, CategoryCreateView,
                    CategoryCreateView, CategoryListView)

urlpatterns = [

    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/', ProductListView.as_view(), name='products'),

    path('categories/<slug:slug>/', CategoryDetail.as_view(), name='category_detail'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('categories', CategoryListView.as_view(), name='categories'),
]