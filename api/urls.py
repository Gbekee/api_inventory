from django.urls import path
from . import views

urlpatterns=[
    path('items', views.items, name='items'),
    path('suppliers', views.suppliers, name='suppliers'),
    path('item/<str:pk>', views.item, name='item'),
    path('supplier/<str:pk>', views.supplier, name='supplier'),
    path('supplier_items/<str:pk>', views.supplier_items, name='supplier_items'),
]
