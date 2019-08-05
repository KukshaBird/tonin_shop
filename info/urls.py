from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'info'

urlpatterns = [
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('deliverance/', views.Deliverance.as_view(), name='deliverance')
]
