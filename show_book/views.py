from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse

#вывод не полной информации
def show_bookview(request):
    show = models.ShowBook.objects.all
    return render(request, 'showbook.html', {'show': show})

#вывод полной информации по id
def show_book_detailview(request, id):
    show_id = get_object_or_404(models.ShowBook, id=id)
    return render(request, 'showbook_detail.html', {'show_id': show_id})

#Добавление книги через формы
def create_show_book_view(request):
    method = request.method
    if method == 'POST':
        form = forms.ShowBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Книга успешно добавлена!<h/2>')
    else:
        form = forms.ShowBookForm()
    return render(request, 'add_showbook.html', {'form': form})


#изменения данных о книги
def update_show_book_view(request, id):
    show_object = get_object_or_404(models.ShowBook, id=id)
    if request.method == 'POST':
        form = forms.ShowBookForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Книга успешно обновлена</h2>')
    else:
        form = forms.ShowBookForm(instance=show_object)
    return render(request, 'update_show_book.html', {
        'form': form,
        'object': show_object
    })

#удаление с базы
def delete_show_book_view(request, id):
    show_object = get_object_or_404(models.ShowBook, id=id)
    show_object.delete()
    return HttpResponse('<h2>Фильм успешно удален</h2>')