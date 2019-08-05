from django.views.generic import TemplateView

# Create your views here.
class Contacts(TemplateView):
    template_name = 'contacts.html'

class Deliverance(TemplateView):
    template_name = 'deliverance.html'
