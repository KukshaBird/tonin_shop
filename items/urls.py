from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'items'

urlpatterns = [
    path('',views.ProductListView.as_view(),name='products_list'),
    path('towels',views.TowelListView.as_view(),name='towels_list'),
    path('details/<int:pk>',views.ProductDetailView.as_view(),name='product_details'),
     path('details/towel/<int:pk>',views.TowelDetailView.as_view(),name='towel_details')
]
