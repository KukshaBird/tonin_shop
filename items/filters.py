import django_filters
from .models import Product
from django_filters.conf import DEFAULTS
from django_filters.widgets import RangeWidget, SuffixedMultiWidget



class ProductFilter(django_filters.FilterSet):

	CHOICES = (
			('ascending', 'От новых к старым'),
			('descending', 'От старых к новым')
		)

	ordering = django_filters.ChoiceFilter(label='Сортировать:', choices=CHOICES, method='filter_by_order')

	class Meta:
		model = Product
		fields = {
			'name': ['icontains'],
			'price': ['lt','gt'],
			'fabric': ['icontains']
		}

	def filter_by_order(self, queryset, name, value):
		expression = 'create_date' if value == 'ascending' else '-create_date'
		return queryset.order_by(expression)


