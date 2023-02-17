from django.shortcuts import render, get_object_or_404
from . import models

#вывод не полной информации
def show_bookview(request):
    show = models.ShowBook.objects.all
    return render(request, 'showbook.html', {'show': show})

#вывод полной информации по id
def show_book_detailview(request, id):
    show_id = get_object_or_404(models.ShowBook, id=id)
    return render(request, 'showbook_detail.html', {'show_id': show_id})