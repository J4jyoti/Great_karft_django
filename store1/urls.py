
from django.urls import path,include
from .import views 

urlpatterns = [
    path('', views.store1, name = 'store1'),
    path('<slug:category_slug>/', views.store1, name = 'products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name = 'product_detail'),
    
]