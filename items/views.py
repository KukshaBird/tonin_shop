from django.views.generic import ListView,DetailView
#from django.http import HttpResponse
from items.models import Product,Towel
#from tonin_shop.views import Index
from .filters import ProductFilter,TowelFilter
from django.core.paginator import Paginator


class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    # queryset = Product.objects.all().order_by('-name')
    paginate_by = 6



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET)
        paginator = Paginator(context['filter'].qs.all().order_by('name'), 6)
        page = self.request.GET.get('page')
        context['paginator'] = paginator.get_page(page)
        if paginator.count > 6:
            context['is_paginated'] = True

        return context

class TowelListView(ListView):
    model = Towel
    template_name = 'towels_list.html'
    paginate_by = 6
    queryset = Towel.objects.all().order_by('-create_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TowelFilter(self.request.GET, queryset=self.get_queryset())
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_types'] = Product.objects.filter(name=context['product'].name)
        return context

class TowelDetailView(DetailView):
    model = Towel
    template_name = 'towel_detail.html'
