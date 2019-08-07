import django_filters
from .models import Product,Towel



class ProductFilter(django_filters.FilterSet):

	CHOICES = (
			('ascending', 'А - Я'),
			('descending', 'Я - А')
		)

	ordering = django_filters.ChoiceFilter(label='Сортировать:', choices=CHOICES, method='filter_by_order')
	price = django_filters.RangeFilter(label='Цена между')
	class Meta:
		model = Product
		fields = {
			'name': ['icontains'],
			'article':['icontains'],
			# 'price': ['range'],
			'fabric': ['exact'],
			'type': ['exact'],
			'available':['exact']
		}

	def filter_by_order(self, queryset, name, value):
		expression = 'name' if value == 'ascending' else '-name'
		return queryset.order_by(expression)

class TowelFilter(django_filters.FilterSet):

	CHOICES = (
			('ascending', 'А - Я'),
			('descending', 'Я - А')
		)

	ordering = django_filters.ChoiceFilter(label='Сортировать:', choices=CHOICES, method='filter_by_order')

	class Meta:
		model = Towel
		fields = {
			'name': ['icontains'],
			'price': ['lt','gt'],
			'fabric': ['icontains']
		}

	def filter_by_order(self, queryset, name, value):
		expression = 'name' if value == 'ascending' else '-name'
		return queryset.order_by(expression)



