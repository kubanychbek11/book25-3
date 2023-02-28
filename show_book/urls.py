from django.urls import path
from . import views

urlpatterns =[
    #path('showbook/', views.show_bookview, name='show'),
    path('showbook/', views.ShowBookView.as_view(), name='show'),
    #path('showbook/<int:id>/', views.show_book_detailview, name='details'),
    path('showbook/<int:id>/', views.ShowBookDetailView.as_view(), name='detail'),
    #path('showbook/<int:id>/update/', views.update_show_book_view, name='update'),
    path('showbook/<int:id>/update/', views.ShowBookUpdateView.as_view(), name='update'),
    #path('showbook/<int:id>/delete/', views.delete_show_book_view, name='delete'),
    path('showbook/<int:id>/delete/', views.ShowBookDeleteView.as_view(), name='delete'),
    #path('add-book/', views.create_show_book_view, name='create'),
    path('add-book/', views.ShowBookCreateView.as_view(), name='create'),
    path('add-comment', views.AddRatingView.as_view(), name='com'),


]