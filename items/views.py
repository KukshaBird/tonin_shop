from django.views.generic import ListView,DetailView
#from django.http import HttpResponse
from items.models import Product,Towel
#from tonin_shop.views import Index
from .filters import ProductFilter


class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'product_list'
    paginate_by = 6
    queryset = Product.objects.all().order_by('-create_date')

#    def get_filter(self):
#        return Product.obejects.all().filter(type__contains='OH')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        #context['product_list'] = Product.objects.all().order_by('-create_date')
        query = self.request.GET.get("q")
        if query:
            context['product.type_list'] = context['product.type_list'].filter(name__icontains=query)
        return context

class TowelListView(ListView):
    model = Towel
    template_name = 'towels_list.html'
    paginate_by = 6
    queryset = Towel.objects.all().order_by('-create_date')

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
