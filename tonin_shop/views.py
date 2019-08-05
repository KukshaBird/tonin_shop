from django.views.generic import TemplateView
#from django.db.models import Count
#from items.models import Product,ProductType

class Index(TemplateView):
#    model = Product
    template_name = 'index.html'

#    def get_context_data(self,**kwargs):
#        context = super().get_context_data(**kwargs)
#        context['products_list'] = ProductType.objects.all()
#        return context
