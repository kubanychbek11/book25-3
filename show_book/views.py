from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic

#вывод не полной информации
class ShowBookView(generic.ListView):
    template_name = 'showbook.html'
    queryset = models.ShowBook.objects.all()

    def get_queryset(self):
        return models.ShowBook.objects.all()


#def show_bookview(request):
#    show = models.ShowBook.objects.all()
#    return render(request, 'showbook.html', {'show': show})

#вывод полной информации по id
class ShowBookDetailView(generic.DetailView):
    template_name = 'showbook_detail.html'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.ShowBook, id=show_id)



#def show_book_detailview(request, id):
#    show_id = get_object_or_404(models.ShowBook, id=id)
#    #return render(request, 'showbook_detail.html', {'show_id': show_id})
#    #book = get_object_or_404(ShowBook, id=id)
#    ratings = show_id.rating_set.all()
#    if ratings:
#        average_rating = sum(r.stars for r in ratings) / len(ratings)
#    else:
#        average_rating = 0
#    context = {
#        'show_id': show_id,
#        'average_rating': average_rating,
#    }
#    return render(request, 'showbook_detail.html', context=context)

#Добавление книги через формы

class ShowBookCreateView(generic.CreateView):
    template_name = 'add_showbook.html'
    form_class = forms.ShowBookForm
    queryset = models.ShowBook.objects.all()
    success_url = '/showbook/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ShowBookCreateView, self).form_valid(form=form)
#def create_show_book_view(request):
#    method = request.method
#    if method == 'POST':
#        form = forms.ShowBookForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return HttpResponse('<h2>Книга успешно добавлена!<h/2>')
#    else:
#        form = forms.ShowBookForm()
#    return render(request, 'add_showbook.html', {'form': form})


#изменения данных о книги
class ShowBookUpdateView(generic.UpdateView):
    template_name = 'update_show_book.html'
    form_class = forms.ShowBookForm
    success_url = '/showbook/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.ShowBook, id=show_id)

    def form_valid(self, form):
        return super(ShowBookUpdateView, self).form_valid(form=form)
#def update_show_book_view(request, id):
#    show_object = get_object_or_404(models.ShowBook, id=id)
#    if request.method == 'POST':
#        form = forms.ShowBookForm(instance=show_object, data=request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponse('<h2>Книга успешно обновлена</h2>')
#    else:
#        form = forms.ShowBookForm(instance=show_object)
#    return render(request, 'update_show_book.html', {
#        'form': form,
#        'object': show_object
#    })

#удаление с базы
class ShowBookDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/show_book/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.ShowBook, id=show_id)
#def delete_show_book_view(request, id):
#    show_object = get_object_or_404(models.ShowBook, id=id)
#    show_object.delete()
#    return HttpResponse('<h2>Фильм успешно удален</h2>')

class AddRatingView(generic.CreateView):
    template_name = 'showbook_detail.html'
    form_class = forms.CommentForm
    queryset = models.RatingBook.objects.all()
    success_url = '/showbook/<int:id>/'

    def form_valid(self, form):
        return super(AddRatingView, self).form_valid(form=form)
