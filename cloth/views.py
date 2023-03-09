from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms

#весь список одежды
class ProductListView(ListView):
    queryset = models.ProductCL.objects.filter().order_by('-id')
    template_name = 'product_list.html'

    def get_queryset(self):
        return models.ProductCL.objects.filter().order_by('-id')

# список одежды по тегу male
class MaleProductListView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='male')
    template_name = 'male_product_list.html'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='male')

# список одежды по тегу female
class FemaleProductListView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='female')
    template_name = 'female_product_list.html'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='female')

# список одежды по тегу kid
class KidProductListView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='kid')
    template_name = 'kid_product_list.html'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='kid')

# список одежды по тегу uni
class UniProductListView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='uni')
    template_name = 'uni_product_list.html'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='uni')


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.ProductCL, id=product_id)

class OrderCreateView(CreateView):
    template_name = 'add_order.html'
    form_class = forms.OrderForm
    success_url = '/products/'
    queryset = models.OrderCL.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)