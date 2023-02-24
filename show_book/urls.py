from django.urls import path
from . import views

urlpatterns =[
    path('showbook/', views.show_bookview, name='show'),
    path('showbook/<int:id>/', views.show_book_detailview, name='details'),
    path('showbook/<int:id>/update/', views.update_show_book_view, name='update'),
    path('showbook/<int:id>/delete/', views.delete_show_book_view, name='delete'),
    path('add-book/', views.create_show_book_view, name='create'),


]