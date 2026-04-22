from django.urls import path
from .views import (
    dashboard,
    product_page,
    sync_data,
    get_products,
    get_products_by_vendor,
    add_inventory
)

urlpatterns = [
    # UI
    path('', dashboard),                      # Dashboard UI
    path('products/', product_page),          # Products UI

    # APIs
    path('api/sync/', sync_data),
    path('api/products/', get_products),
    path('api/add/', add_inventory),
    path('api/products/vendor/<str:vendor_name>/', get_products_by_vendor),
]