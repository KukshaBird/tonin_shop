from django import forms

class ProductFilterForm(forms.Form):
	name = forms.CharField(label='Наименование', max_length=100)