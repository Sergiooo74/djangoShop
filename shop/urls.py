from django.urls import path
from .views import ProductListView, CategoryCreateView

urlpatterns = [
    path('product/', ProductListView.as_view(), name='products'),

    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),

]