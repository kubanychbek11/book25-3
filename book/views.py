from django.http import HttpResponse
from django.shortcuts import render
from . import models
from book.models import *

def book_view(request):
    book = Book.objects.all
    return render(request, 'book.html', {'book': book})