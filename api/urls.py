from django.urls import path
from . import views

urlpatterns=[
    path('items', views.items, name='items'),
    path('suppliers', views.suppliers, name='suppliers'),
    path('items/<str:pk>', views.item, name='item'),
    path('suppliers/<str:pk>', views.supplier, name='supplier'),
]
