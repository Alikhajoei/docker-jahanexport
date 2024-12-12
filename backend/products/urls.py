from django.urls import path
from . import views
urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/<slug:slug>/', views.ProductsListView.as_view(), name='products'),
    path('', views.ProductsListView.as_view(), name='products_all'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),  # جزئیات محصول
]
