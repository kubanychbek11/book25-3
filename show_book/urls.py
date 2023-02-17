from django.urls import path
from . import views

urlpatterns =[
    path('showbook/', views.show_bookview, name='show'),
    path('showbook/<int:id>/', views.show_book_detailview, name='details'),

]