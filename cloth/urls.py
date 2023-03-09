from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:id>/', views.ProductDetailView.as_view(), name='detail'),
    path('add-order/', views.OrderCreateView.as_view(), name='add'),
    path('male/', views.MaleProductListView.as_view(), name='male'),
    path('female/', views.FemaleProductListView.as_view(), name='female'),
    path('kid/', views.KidProductListView.as_view(), name='kid'),
    path('uni/', views.UniProductListView.as_view(), name='uni'),
]