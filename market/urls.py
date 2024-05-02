from django.urls import path

from market.views import (
    CreateProductView,
    DetailedProductView,
    ProductListView,
    DeleteProductView,
    UpdateProductView,
    APIRoot,
)

urlpatterns = [
    path('', APIRoot.as_view(), name='api-root'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', CreateProductView.as_view(), name='create_product'),
    path('products/<int:pk>/', DetailedProductView.as_view(), name='detailed_product'),
    path('products/<int:pk>/delete/', DeleteProductView.as_view(), name='delete_product'),
    path('products/<int:pk>/update/', UpdateProductView.as_view(), name='update_product'),
]
